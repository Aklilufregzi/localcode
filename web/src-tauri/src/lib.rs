use serde::Serialize;
use std::{path::{Path, PathBuf}, process::Stdio, sync::Mutex};
use tauri::{AppHandle, Emitter, Manager};
use tokio::{fs, process::Command, time::{sleep, Duration}};

const MODEL: &str = "qwen2.5-coder:1.5b";
struct Runner(Mutex<Option<std::process::Child>>);

#[derive(Clone, Serialize)]
#[serde(rename_all = "camelCase")]
struct LocalStatus { python: bool, python_ready: bool, typescript: bool, ollama: bool, model: bool, model_name: String, workspace: String }
#[derive(Clone, Serialize)]
struct SetupProgress { stage: String, percent: u8, message: String }

fn progress(app: &AppHandle, stage: &str, percent: u8, message: impl Into<String>) {
  let _ = app.emit("localquest:setup-progress", SetupProgress { stage: stage.into(), percent, message: message.into() });
}
fn app_root(app: &AppHandle) -> Result<PathBuf, String> { app.path().app_data_dir().map_err(|e| e.to_string()) }
fn workspace(app: &AppHandle) -> Result<PathBuf, String> { Ok(app_root(app)?.join("practice")) }
fn venv_python(app: &AppHandle) -> Result<PathBuf, String> { Ok(app_root(app)?.join("runtime/python").join(if cfg!(windows) { "Scripts/python.exe" } else { "bin/python" })) }

async fn command_works(program: &str, args: &[&str]) -> bool {
  Command::new(program).args(args).stdout(Stdio::null()).stderr(Stdio::null()).status().await.map(|s| s.success()).unwrap_or(false)
}
async fn python_command() -> Option<String> {
  let choices: &[&str] = if cfg!(windows) { &["py", "python"] } else { &["python3", "python"] };
  for item in choices { if command_works(item, &["--version"]).await { return Some((*item).into()); } }
  None
}
async fn ollama_command() -> Option<PathBuf> {
  let mut candidates = Vec::new();
  if cfg!(target_os = "macos") {
    if let Ok(home) = std::env::var("HOME") { candidates.push(PathBuf::from(home).join("Applications/Ollama.app/Contents/Resources/ollama")); }
    candidates.extend([PathBuf::from("/Applications/Ollama.app/Contents/Resources/ollama"), PathBuf::from("/usr/local/bin/ollama"), PathBuf::from("/opt/homebrew/bin/ollama")]);
  } else if cfg!(windows) {
    if let Ok(base) = std::env::var("LOCALAPPDATA") { candidates.push(PathBuf::from(base).join("Programs/Ollama/ollama.exe")); }
  } else { candidates.extend([PathBuf::from("/usr/local/bin/ollama"), PathBuf::from("/usr/bin/ollama")]); }
  candidates.into_iter().find(|path| path.exists())
}
async fn ollama_state() -> (bool, bool) {
  let response = match reqwest::get("http://127.0.0.1:11434/api/tags").await { Ok(v) => v, Err(_) => return (false, false) };
  if !response.status().is_success() { return (false, false); }
  let value: serde_json::Value = response.json().await.unwrap_or_default();
  let model = value["models"].as_array().map(|items| items.iter().any(|item| item["name"].as_str().map(|name| name == MODEL || name.starts_with(&format!("{MODEL}:"))).unwrap_or(false))).unwrap_or(false);
  (true, model)
}

#[tauri::command]
async fn system_status(app: AppHandle) -> Result<LocalStatus, String> {
  let python = python_command().await.is_some();
  let python_ready = venv_python(&app)?.exists();
  let (ollama, model) = ollama_state().await;
  Ok(LocalStatus { python, python_ready, typescript: true, ollama, model, model_name: MODEL.into(), workspace: workspace(&app)?.display().to_string() })
}
async fn run_checked(program: impl AsRef<Path>, args: &[&str]) -> Result<(), String> {
  let output = Command::new(program.as_ref()).args(args).output().await.map_err(|e| e.to_string())?;
  if output.status.success() { Ok(()) } else { Err(String::from_utf8_lossy(&output.stderr).trim().to_string()) }
}

#[tauri::command]
async fn setup_python(app: AppHandle) -> Result<LocalStatus, String> {
  let python = python_command().await.ok_or("Python 3 is not installed yet. Use the download button, install it, then retry.")?;
  let executable = venv_python(&app)?;
  let runtime = executable.parent().and_then(Path::parent).ok_or("Could not create the Python runtime path")?;
  fs::create_dir_all(runtime.parent().unwrap_or(runtime)).await.map_err(|e| e.to_string())?;
  progress(&app, "python", 10, "Creating a private Python environment…");
  if !executable.exists() { run_checked(&python, &["-m", "venv", runtime.to_str().ok_or("Invalid runtime path")?]).await?; }
  progress(&app, "python", 55, "Installing the local test runner…");
  run_checked(&executable, &["-m", "pip", "install", "--disable-pip-version-check", "pytest"]).await?;
  progress(&app, "python", 100, "Python lab ready.");
  system_status(app).await
}
async fn wait_for_ollama() -> Result<(), String> {
  for _ in 0..90 { if ollama_state().await.0 { return Ok(()); } sleep(Duration::from_millis(500)).await; }
  Err("Ollama installed, but its local service did not start.".into())
}

#[tauri::command]
async fn setup_ollama(app: AppHandle) -> Result<LocalStatus, String> {
  if let Some(command) = ollama_command().await {
    let _ = Command::new(command).arg("serve").stdout(Stdio::null()).stderr(Stdio::null()).spawn();
    wait_for_ollama().await?; progress(&app, "ollama", 100, "Local AI engine ready."); return system_status(app).await;
  }
  #[cfg(target_os = "macos")]
  {
    progress(&app, "ollama", 2, "Downloading Ollama from the official release…");
    let bytes = reqwest::get("https://ollama.com/download/Ollama-darwin.zip").await.map_err(|e| e.to_string())?.error_for_status().map_err(|e| e.to_string())?.bytes().await.map_err(|e| e.to_string())?;
    let setup = std::env::temp_dir().join("localquest-ollama"); let archive = setup.join("Ollama-darwin.zip"); let unpacked = setup.join("unpacked");
    let target = PathBuf::from(std::env::var("HOME").map_err(|_| "Cannot locate your home folder")?).join("Applications/Ollama.app");
    let _ = fs::remove_dir_all(&setup).await; fs::create_dir_all(&unpacked).await.map_err(|e| e.to_string())?; fs::write(&archive, bytes).await.map_err(|e| e.to_string())?;
    progress(&app, "ollama", 88, "Verifying and installing Ollama…");
    run_checked("/usr/bin/ditto", &["-x", "-k", archive.to_str().unwrap(), unpacked.to_str().unwrap()]).await?;
    let source = unpacked.join("Ollama.app"); run_checked("/usr/bin/codesign", &["--verify", "--deep", "--strict", source.to_str().unwrap()]).await?;
    fs::create_dir_all(target.parent().unwrap()).await.map_err(|e| e.to_string())?; if target.exists() { fs::remove_dir_all(&target).await.map_err(|e| e.to_string())?; }
    run_checked("/usr/bin/ditto", &[source.to_str().unwrap(), target.to_str().unwrap()]).await?; Command::new("/usr/bin/open").arg(&target).spawn().map_err(|e| e.to_string())?;
    wait_for_ollama().await?; progress(&app, "ollama", 100, "Local AI engine ready."); system_status(app).await
  }
  #[cfg(not(target_os = "macos"))]
  Err("Automatic Ollama installation is currently available in the macOS build. Open the official installer, then retry.".into())
}

#[tauri::command]
async fn setup_model(app: AppHandle) -> Result<LocalStatus, String> {
  let command = ollama_command().await.ok_or("Install Ollama first, then retry the model download.")?;
  progress(&app, "model", 5, format!("Downloading {MODEL}…")); run_checked(command, &["pull", MODEL]).await?;
  progress(&app, "model", 100, "Byte is ready for takeoff."); system_status(app).await
}

#[tauri::command]
async fn open_download(target: String) -> Result<(), String> {
  let url = if target == "python" { "https://www.python.org/downloads/" } else { "https://ollama.com/download" };
  let status = if cfg!(target_os = "macos") { Command::new("/usr/bin/open").arg(url).status().await } else if cfg!(windows) { Command::new("cmd").args(["/C", "start", "", url]).status().await } else { Command::new("xdg-open").arg(url).status().await };
  status.map_err(|e| e.to_string()).and_then(|s| if s.success() { Ok(()) } else { Err("Could not open the download page".into()) })
}

#[tauri::command]
async fn runner_request(method: String, path: String, body: Option<serde_json::Value>) -> Result<serde_json::Value, String> {
  if !matches!(path.as_str(), "/api/problems" | "/api/run" | "/api/review" | "/api/solution") && !path.starts_with("/api/problems/") {
    return Err("Unsupported local runner request".into());
  }
  let url = format!("http://127.0.0.1:4311{path}");
  let client = reqwest::Client::new();
  let response = if method == "POST" { client.post(url).json(&body.unwrap_or_default()).send().await } else { client.get(url).send().await }.map_err(|e| format!("Local runner is unavailable: {e}"))?;
  let status = response.status();
  let value: serde_json::Value = response.json().await.map_err(|e| format!("Local runner returned invalid data: {e}"))?;
  if status.is_success() { Ok(value) } else { Err(value["error"].as_str().unwrap_or("Local runner request failed").into()) }
}

fn copy_tree(source: &Path, target: &Path, skip_node_modules: bool) -> std::io::Result<()> {
  std::fs::create_dir_all(target)?;
  for entry in std::fs::read_dir(source)? { let entry = entry?; let name = entry.file_name(); let from = entry.path(); let to = target.join(&name);
    if name == ".venv" || name == "__pycache__" || (skip_node_modules && name == "node_modules") { continue; }
    if from.is_dir() { copy_tree(&from, &to, skip_node_modules)?; } else { std::fs::copy(from, to)?; }
  } Ok(())
}
fn development_root() -> PathBuf { PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("../..") }
fn prepare_workspace(app: &AppHandle) -> Result<PathBuf, String> {
  let target = workspace(app)?; if target.join("python").exists() && target.join("typescript").exists() { return Ok(target); }
  let source = if cfg!(debug_assertions) { development_root() } else { app.path().resource_dir().map_err(|e| e.to_string())?.join("practice") };
  copy_tree(&source.join("python"), &target.join("python"), true).map_err(|e| e.to_string())?; copy_tree(&source.join("typescript"), &target.join("typescript"), true).map_err(|e| e.to_string())?; Ok(target)
}
fn start_runner(app: &AppHandle) -> Result<std::process::Child, String> {
  let root = prepare_workspace(app)?; let resource = app.path().resource_dir().map_err(|e| e.to_string())?;
  let bundled_node = if cfg!(windows) { resource.join("runtime/node.exe") } else { resource.join("runtime/node") };
  let (node, runner, modules) = if cfg!(debug_assertions) { (PathBuf::from("node"), development_root().join("web/runner.mjs"), development_root().join("typescript/node_modules")) } else { (bundled_node, resource.join("runner.mjs"), resource.join("typescript-runtime/node_modules")) };
  let child = std::process::Command::new(node).arg(runner).env("LOCALQUEST_ROOT", &root).env("LOCALQUEST_PYTHON", venv_python(app)?).env("LOCALQUEST_TSX", modules.join("tsx/dist/cli.mjs")).env("LOCALQUEST_VITEST", modules.join("vitest/vitest.mjs")).stdout(Stdio::inherit()).stderr(Stdio::inherit()).spawn().map_err(|e| format!("Could not start the local code runner: {e}"))?;
  for _ in 0..60 { if std::net::TcpStream::connect("127.0.0.1:4311").is_ok() { return Ok(child); } std::thread::sleep(std::time::Duration::from_millis(50)); }
  Err("The local code runner did not become ready in time.".into())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
  tauri::Builder::default().manage(Runner(Mutex::new(None))).setup(|app| {
    if cfg!(debug_assertions) { app.handle().plugin(tauri_plugin_log::Builder::default().level(log::LevelFilter::Info).build())?; }
    let child = start_runner(app.handle()).map_err(std::io::Error::other)?; *app.state::<Runner>().0.lock().unwrap() = Some(child); Ok(())
  }).on_window_event(|window, event| if matches!(event, tauri::WindowEvent::Destroyed) { if let Some(mut child) = window.state::<Runner>().0.lock().unwrap().take() { let _ = child.kill(); } })
    .invoke_handler(tauri::generate_handler![system_status, setup_python, setup_ollama, setup_model, open_download, runner_request]).run(tauri::generate_context!()).expect("error while running LocalQuest");
}

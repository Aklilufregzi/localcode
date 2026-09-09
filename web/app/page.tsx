"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import type { CSSProperties, PointerEvent as ReactPointerEvent } from "react";
import Editor from "@monaco-editor/react";
import type { editor as MonacoEditor } from "monaco-editor";
import { AuthGate, useAuth } from "./auth";
import { DesktopSetup } from "./desktop-setup";
import { supabase } from "./supabase";
import { Landing } from "./landing";
type Problem = {
  id: string;
  title: string;
  topic: string;
  difficulty?: string;
  languages: string[];
  completed?: string[];
};
type Detail = Problem & {
  number?: string;
  difficulty?: string;
  url?: string;
  description: string;
  code: Record<string, string>;
  tests: Record<string, string>;
  examples?: { name: string; code?: string; input?: string; output?: string }[];
};
type Review = {
  summary: string;
  comments: {
    line: number;
    kind: "praise" | "roast" | "tip";
    message: string;
  }[];
};
type SolutionStep = { title: string; explanation: string; code: string };
type RunResult = { output?: string; submitted?: boolean };
const responseJson = <T,>(response: Response) => response.json() as Promise<T>;
const fallback: Detail = {
  id: "arrays-hashing/contains-duplicate",
  title: "Contains Duplicate",
  topic: "Arrays & Hashing",
  languages: ["typescript", "python"],
  description:
    "Given an integer array nums, return true if any value appears at least twice. Return false when every element is distinct.",
  code: {
    typescript:
      "export function containsDuplicate(nums: number[]): boolean {\n  const seen = new Set<number>();\n\n  for (const num of nums) {\n    // Try a breakpoint here\n    if (seen.has(num)) return true;\n    seen.add(num);\n  }\n\n  return false;\n}",
    python: "",
  },
  tests: { typescript: "4 local test cases", python: "4 local test cases" },
};

function PracticeApp() {
  const { user } = useAuth();
  const [problems, setProblems] = useState<Problem[]>([fallback]);
  const [selected, setSelected] = useState<Detail>(fallback);
  const [language, setLanguage] = useState("typescript");
  const [code, setCode] = useState(fallback.code.typescript);
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("All topics");
  const [showList, setShowList] = useState(
    () =>
      typeof window === "undefined" ||
      localStorage.getItem("localcode.showList") !== "false",
  );
  const [showDescription, setShowDescription] = useState(
    () =>
      typeof window === "undefined" ||
      localStorage.getItem("localcode.showDescription") !== "false",
  );
  const [output, setOutput] = useState("Loading your local exercise…");
  const [running, setRunning] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const [coachOn, setCoachOn] = useState(false);
  const [voiceOn, setVoiceOn] = useState(false);
  const [voiceStatus, setVoiceStatus] = useState<"off" | "ready">("off");
  const [review, setReview] = useState<Review | null>(null);
  const [reviewing, setReviewing] = useState(false);
  const [reviewError, setReviewError] = useState("");
  const [outputHeight, setOutputHeight] = useState(190);
  const [solutionSteps, setSolutionSteps] = useState<SolutionStep[]>([]);
  const [solutionIndex, setSolutionIndex] = useState(-1);
  const [solutionLoading, setSolutionLoading] = useState(false);
  const attemptBeforeSolution = useRef("");
  const spokenReview = useRef("");
  const lastSpokenCode = useRef(fallback.code.typescript);
  const voiceEditCount = useRef(0);
  const lastVoiceBargeIn = useRef(0);
  const editorRef = useRef<MonacoEditor.IStandaloneCodeEditor | null>(null);
  const zoneIds = useRef<string[]>([]);
  useEffect(() => {
    Promise.all([
      fetch("http://localhost:4311/api/problems").then(responseJson<Problem[]>),
      fetch(`http://localhost:4311/api/problems/${fallback.id}`).then(
        responseJson<Detail>,
      ),
    ])
      .then(([items, d]) => {
        setProblems(items);
        setSelected(d);
        setLanguage("typescript");
        setCode(d.code.typescript ?? "");
        setOutput("Ready. Run the tests when you are done.");
        setLoaded(true);
      })
      .catch(() =>
        setOutput(
          "Runner is offline. Start the app with npm run dev from the web folder.",
        ),
      );
  }, []);
  useEffect(() => {
    if (!user || !supabase) return;
    supabase
      .from("problem_progress")
      .select("problem_id,language")
      .eq("completed", true)
      .then(({ data, error }) => {
        if (error) {
          setReviewError(`Progress sync: ${error.message}`);
          return;
        }
        const done = new Map<string, string[]>();
        for (const row of data ?? [])
          done.set(row.problem_id, [
            ...(done.get(row.problem_id) ?? []),
            row.language,
          ]);
        setProblems((items) =>
          items.map((item) => ({
            ...item,
            completed: done.get(item.id) ?? [],
          })),
        );
      });
  }, [user]);
  async function choose(p: Problem) {
    setSolutionIndex(-1);
    setSolutionSteps([]);
    setLoaded(false);
    try {
      const d = await fetch(`http://localhost:4311/api/problems/${p.id}`).then(
        responseJson<Detail>,
      );
      setSelected(d);
      setLanguage(d.languages[0]);
      setCode(d.code[d.languages[0]] ?? "");
      setOutput("Ready.");
      setLoaded(true);
    } catch {
      setSelected({ ...fallback, ...p });
      setOutput("Could not load this exercise.");
    }
  }
  function switchLanguage(next: string) {
    setSolutionIndex(-1);
    setSolutionSteps([]);
    setLanguage(next);
    setCode(selected.code[next] ?? "");
    setOutput("Ready.");
  }
  async function openSolution() {
    if (solutionIndex >= 0) return;
    attemptBeforeSolution.current = code;
    setSolutionLoading(true);
    setReviewError("");
    try {
      const response = await fetch("http://localhost:4311/api/solution", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ id: selected.id, language, code }),
      });
      const result = await responseJson<{
        steps: SolutionStep[];
        error?: string;
      }>(response);
      if (!response.ok) throw new Error(result.error);
      setSolutionSteps(result.steps);
      setSolutionIndex(0);
      setCode(result.steps[0].code);
    } catch (error) {
      setReviewError((error as Error).message);
    } finally {
      setSolutionLoading(false);
    }
  }
  function goToSolutionStep(next: number) {
    const bounded = Math.max(0, Math.min(solutionSteps.length - 1, next));
    setSolutionIndex(bounded);
    setCode(solutionSteps[bounded].code);
  }
  function closeSolution() {
    setCode(attemptBeforeSolution.current);
    setSolutionIndex(-1);
    setSolutionSteps([]);
  }
  useEffect(() => {
    lastSpokenCode.current = code;
    voiceEditCount.current = 0;
  }, [selected.id, language]);
  useEffect(() => {
    if (!coachOn || !loaded || !code.trim() || solutionIndex >= 0) return;
    const controller = new AbortController();
    const timer = setTimeout(async () => {
      setReview(null);
      setReviewing(true);
      setReviewError("");
      try {
        const response = await fetch("http://localhost:4311/api/review", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ id: selected.id, language, code }),
          signal: controller.signal,
        });
        const result = await responseJson<Review & { error?: string }>(
          response,
        );
        if (!response.ok) throw new Error(result.error);
        setReview(result);
      } catch (error) {
        if ((error as Error).name !== "AbortError")
          setReviewError((error as Error).message);
      } finally {
        if (!controller.signal.aborted) setReviewing(false);
      }
    }, 850);
    return () => {
      clearTimeout(timer);
      controller.abort();
    };
  }, [code, language, selected.id, coachOn, loaded, solutionIndex]);
  function toggleVoice() {
    if (voiceOn) {
      setVoiceOn(false);
      speechSynthesis.cancel();
      setVoiceStatus("off");
      return;
    }
    setVoiceOn(true);
    lastSpokenCode.current = code;
    voiceEditCount.current = 0;
    lastVoiceBargeIn.current = Date.now();
    setVoiceStatus("ready");
  }
  useEffect(() => () => speechSynthesis.cancel(), []);
  useEffect(() => {
    if (voiceOn && voiceStatus === "ready" && solutionIndex < 0)
      voiceEditCount.current += 1;
  }, [code, voiceOn, voiceStatus, solutionIndex]);
  useEffect(() => {
    if (
      !coachOn ||
      !voiceOn ||
      voiceStatus !== "ready" ||
      !review ||
      solutionIndex >= 0
    )
      return;
    const before = lastSpokenCode.current;
    let prefix = 0;
    while (
      prefix < before.length &&
      prefix < code.length &&
      before[prefix] === code[prefix]
    )
      prefix++;
    let suffix = 0;
    while (
      suffix < before.length - prefix &&
      suffix < code.length - prefix &&
      before[before.length - 1 - suffix] === code[code.length - 1 - suffix]
    )
      suffix++;
    const changedChars = Math.max(
      before.length - prefix - suffix,
      code.length - prefix - suffix,
    );
    const changedLines = Math.abs(
      before.split("\n").length - code.split("\n").length,
    );
    const majorChange = changedChars >= 90 || changedLines >= 3;
    const struggling = voiceEditCount.current >= 18;
    const cooledDown = Date.now() - lastVoiceBargeIn.current >= 25000;
    if (!cooledDown || (!majorChange && !struggling)) return;
    const reaction = review.comments[0]?.message || review.summary;
    const speech = reaction.trim().split(/\s+/).slice(0, 12).join(" ");
    if (!speech || speech === spokenReview.current) return;
    spokenReview.current = speech;
    lastSpokenCode.current = code;
    voiceEditCount.current = 0;
    lastVoiceBargeIn.current = Date.now();
    speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(speech);
    utterance.rate = 1.12;
    utterance.pitch = 1.05;
    speechSynthesis.speak(utterance);
  }, [review, coachOn, voiceOn, voiceStatus, solutionIndex, code]);
  useEffect(() => {
    if (solutionIndex < 0 || !voiceOn || voiceStatus !== "ready") return;
    const step = solutionSteps[solutionIndex];
    if (!step) return;
    const stepNumber = solutionIndex + 1;
    const speech = `Step ${stepNumber}. ${step.explanation}`;
    speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(speech);
    utterance.rate = 1.08;
    speechSynthesis.speak(utterance);
  }, [solutionIndex, solutionSteps, selected.title, voiceOn, voiceStatus]);
  useEffect(() => {
    const instance = editorRef.current;
    if (!instance) return;
    instance.changeViewZones((accessor) => {
      zoneIds.current.forEach((id) => accessor.removeZone(id));
      zoneIds.current = [];
      if (!coachOn || !review || solutionIndex >= 0) return;
      const lineCount = instance.getModel()?.getLineCount() ?? 0;
      for (const comment of review.comments.slice(0, 10)) {
        if (comment.line < 1 || comment.line > lineCount) continue;
        const node = document.createElement("div");
        node.className = `inline-roast ${comment.kind}`;
        const label = document.createElement("b");
        label.textContent =
          comment.kind === "praise" ? "BYTE APPROVES" : "BYTE";
        const message = document.createElement("span");
        message.textContent = comment.message;
        node.appendChild(label);
        node.appendChild(message);
        zoneIds.current.push(
          accessor.addZone({
            afterLineNumber: comment.line,
            heightInLines: 2,
            domNode: node,
          }),
        );
      }
    });
  }, [review, coachOn, solutionIndex]);
  function beginResize(event: ReactPointerEvent) {
    event.preventDefault();
    const startY = event.clientY,
      startHeight = outputHeight;
    const move = (e: PointerEvent) =>
      setOutputHeight(
        Math.max(
          110,
          Math.min(
            window.innerHeight * 0.55,
            startHeight - (e.clientY - startY),
          ),
        ),
      );
    const stop = () => {
      window.removeEventListener("pointermove", move);
      window.removeEventListener("pointerup", stop);
    };
    window.addEventListener("pointermove", move);
    window.addEventListener("pointerup", stop);
  }
  async function execute(action: "run" | "debug" | "submit") {
    setRunning(true);
    setOutput(
      action === "submit"
        ? "Checking submission…"
        : action === "debug"
          ? "Running script with debug diagnostics…"
          : "Running code…",
    );
    try {
      const r = await fetch("http://localhost:4311/api/run", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ id: selected.id, language, code, action }),
      });
      const result = await responseJson<RunResult>(r);
      setOutput(
        result.output ||
          "Script finished without printing anything. Add console.log(...) or print(...) to inspect values.",
      );
      if (result.submitted) {
        setProblems((items) =>
          items.map((item) =>
            item.id === selected.id
              ? {
                  ...item,
                  completed: [
                    ...new Set([...(item.completed ?? []), language]),
                  ],
                }
              : item,
          ),
        );
        if (user && supabase) {
          const { error } = await supabase
            .from("problem_progress")
            .upsert(
              {
                user_id: user.id,
                problem_id: selected.id,
                language,
                completed: true,
                completed_at: new Date().toISOString(),
              },
              { onConflict: "user_id,problem_id,language" },
            );
          if (error)
            setOutput(
              `${result.output}\n\nProgress sync failed: ${error.message}`,
            );
        }
      }
    } catch {
      setOutput(
        "Runner is offline. Start the app with npm run dev from the web folder.",
      );
    } finally {
      setRunning(false);
    }
  }
  const categories = useMemo(
    () => [...new Set(problems.map((problem) => problem.topic))].sort(),
    [problems],
  );
  const visible = useMemo(
    () =>
      problems.filter(
        (p) =>
          (category === "All topics" || p.topic === category) &&
          `${p.title} ${p.topic}`.toLowerCase().includes(query.toLowerCase()),
      ),
    [problems, query, category],
  );
  const completedProblems = problems.filter(
    (problem) => problem.completed?.length,
  );
  const completedEasy = completedProblems.filter(
    (problem) => problem.difficulty === "Easy",
  ).length;
  const isUnlocked = (problem: Problem) => {
    if (problem.completed?.length) return true;
    const path = problems.filter((item) => item.topic === problem.topic);
    const index = path.findIndex((item) => item.id === problem.id);
    if (index === 0)
      return (
        problem.difficulty === "Easy" ||
        problem.difficulty === "Practice" ||
        completedEasy >= 5
      );
    return Boolean(path[index - 1]?.completed?.length);
  };
  const completedCount = completedProblems.length;
  const xp = completedCount * 100;
  const level = Math.floor(xp / 500) + 1;
  const levelProgress = xp % 500;
  const unlockedCount = problems.filter(isUnlocked).length;
  return (
    <main className="app-shell">
      <header className="topbar game-topbar">
        <div className="brand">
          <span className="brand-mark">N</span>
          <span>
            local<span className="accent">quest</span>
          </span>
        </div>
        <div className="layout-controls">
          <button
            className={showList ? "active" : ""}
            aria-pressed={showList}
            onClick={() =>
              setShowList((value) => {
                localStorage.setItem("localcode.showList", String(!value));
                return !value;
              })
            }
          >
            ☷ Quest Map
          </button>
          <button
            className={showDescription ? "active" : ""}
            aria-pressed={showDescription}
            onClick={() =>
              setShowDescription((value) => {
                localStorage.setItem(
                  "localcode.showDescription",
                  String(!value),
                );
                return !value;
              })
            }
          >
            ▤ Mission
          </button>
        </div>
        <div className="game-hud">
          <span className="level-badge">LVL {level}</span>
          <div className="xp-meter">
            <div>
              <b>{xp} XP</b>
              <small>{500 - levelProgress} to next level</small>
            </div>
            <i>
              <span style={{ width: `${levelProgress / 5}%` }} />
            </i>
          </div>
          <span className="trophy">🏆 {completedCount}</span>
          {user && (
            <div className="auth-account">
              <span title={user.email}>{user.email}</span>
              <button onClick={() => supabase?.auth.signOut()}>Sign out</button>
            </div>
          )}
        </div>
      </header>
      <section
        className={`workspace ${showList ? "" : "hide-list"} ${showDescription ? "" : "hide-description"}`}
      >
        <aside className="problem-list quest-list">
          <div className="list-head">
            <div className="list-title">
              <h1>Quest Map</h1>
              <span>
                {unlockedCount}/{problems.length} unlocked
              </span>
            </div>
            <div className="quest-rule">
              ⚡ Clear a quest to unlock the next challenge
            </div>
            <input
              aria-label="Search quests"
              placeholder="Search quests…"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <select
              aria-label="Filter by world"
              value={category}
              onChange={(e) => setCategory(e.target.value)}
            >
              <option value="All topics">All worlds</option>
              {categories.map((name) => (
                <option key={name}>{name}</option>
              ))}
            </select>
          </div>
          <div className="problem-scroll">
            {visible.map((p, i) => {
              const unlocked = isUnlocked(p);
              return (
                <button
                  className={`problem-row quest-row ${p.id === selected.id ? "active" : ""} ${unlocked ? "unlocked" : "locked"}`}
                  key={p.id}
                  onClick={() => unlocked && choose(p)}
                  disabled={!unlocked}
                  title={
                    unlocked ? p.title : "Complete the previous quest to unlock"
                  }
                >
                  <span
                    className={`number ${p.completed?.length ? "done" : ""}`}
                  >
                    {p.completed?.length
                      ? "★"
                      : unlocked
                        ? String(i + 1).padStart(2, "0")
                        : "🔒"}
                  </span>
                  <span>
                    <b>{p.title}</b>
                    <small>
                      {p.topic} · {p.difficulty ?? "Practice"}
                    </small>
                  </span>
                  <em>
                    {unlocked
                      ? p.completed?.length
                        ? "+100 XP"
                        : p.languages.length === 2
                          ? "PY · TS"
                          : p.languages[0] === "python"
                            ? "PY"
                            : "TS"
                      : "LOCKED"}
                  </em>
                </button>
              );
            })}
          </div>
        </aside>
        <section className="problem-pane">
          <div className="pane-tabs">
            <span className="selected">Description</span>
            <span>{selected.examples?.length ?? 0} examples</span>
          </div>
          <article className="statement">
            <div className="problem-kicker">
              <span className="topic-label">{selected.topic}</span>
              {selected.number && <span>#{selected.number}</span>}
            </div>
            <h2>{selected.title}</h2>
            <div
              className={`difficulty ${(selected.difficulty ?? "practice").toLowerCase()}`}
            >
              {selected.difficulty ?? "Practice"}
            </div>
            <p className="problem-description">{selected.description}</p>
            {selected.url && (
              <a
                className="source-link"
                href={selected.url}
                target="_blank"
                rel="noreferrer"
              >
                Open original problem ↗
              </a>
            )}
            <h3>Examples & local cases</h3>
            <div className="examples-list">
              {selected.examples?.length ? (
                selected.examples.map((example, index) => (
                  <section
                    className="example-card"
                    key={`${example.name}-${index}`}
                  >
                    <header>
                      <span>Example {index + 1}</span>
                      <b>{example.name}</b>
                    </header>
                    {example.input !== undefined ? (
                      <div className="example-fields">
                        <div>
                          <b>Input</b>
                          <code>{example.input}</code>
                        </div>
                        <div>
                          <b>Expected output</b>
                          <code>{example.output}</code>
                        </div>
                      </div>
                    ) : (
                      <pre>{example.code}</pre>
                    )}
                  </section>
                ))
              ) : (
                <div className="example">
                  <span>Test coverage</span>
                  <code>
                    {selected.tests[language] ?? "Tests available locally"}
                  </code>
                </div>
              )}
            </div>
            <div className="test-summary">
              <span>{selected.tests[language] ?? "Local tests ready"}</span>
              <span>
                {selected.languages
                  .map((value) => (value === "typescript" ? "TS" : "PY"))
                  .join(" · ")}
              </span>
            </div>
            <p className="hint">
              Run explores your manual examples. Submit checks every local case
              and records completion.
            </p>
          </article>
        </section>
        <section
          className="code-pane"
          style={{ "--output-height": `${outputHeight}px` } as CSSProperties}
        >
          <div className="code-head">
            <div className="language-tabs">
              {selected.languages.map((lang) => (
                <button
                  key={lang}
                  className={lang === language ? "active" : ""}
                  onClick={() => switchLanguage(lang)}
                >
                  {lang === "typescript" ? "TypeScript" : "Python"}
                </button>
              ))}
            </div>
            <div className="run-actions">
              <button
                className={`solution-toggle ${solutionIndex >= 0 ? "on" : ""}`}
                onClick={solutionIndex >= 0 ? closeSolution : openSolution}
                disabled={solutionLoading || !loaded}
              >
                {solutionLoading
                  ? "Preparing…"
                  : solutionIndex >= 0
                    ? "Exit Steps"
                    : "Solution Steps"}
              </button>
              <button
                className={`coach-toggle ${coachOn ? "on" : ""}`}
                onClick={() => setCoachOn((value) => !value)}
              >
                🔥 Byte {coachOn ? (reviewing ? "watching…" : "On") : "Off"}
              </button>
              {coachOn && (
                <button
                  className={`voice-toggle ${voiceStatus}`}
                  title={
                    voiceOn
                      ? "Turn off local spoken reactions"
                      : "Read Qwen reactions aloud on this computer"
                  }
                  aria-label={
                    voiceOn
                      ? "Turn off local spoken reactions"
                      : "Turn on local spoken reactions"
                  }
                  onClick={toggleVoice}
                >
                  {voiceOn ? "🔊" : "🔇"}
                </button>
              )}
              <button
                className="secondary"
                onClick={() => execute("run")}
                disabled={running || !loaded}
              >
                ▶ Run
              </button>
              <button
                className="secondary"
                onClick={() => execute("debug")}
                disabled={running || !loaded}
              >
                ◆ Debug
              </button>
              <button
                onClick={() => execute("submit")}
                disabled={running || !loaded}
              >
                {running ? "Working…" : "Submit"}
              </button>
            </div>
          </div>
          <div className="editor-wrap">
            <Editor
              height="100%"
              language={language}
              theme="vs-dark"
              value={code}
              onMount={(instance) => {
                editorRef.current = instance;
              }}
              onChange={(value) => setCode(value ?? "")}
              loading={<div className="editor-loading">Loading editor…</div>}
              options={{
                fontSize: 14,
                fontFamily:
                  "JetBrains Mono, SFMono-Regular, Consolas, monospace",
                fontLigatures: true,
                lineHeight: 22,
                minimap: { enabled: false },
                scrollBeyondLastLine: false,
                automaticLayout: true,
                tabSize: 2,
                insertSpaces: true,
                readOnly: solutionIndex >= 0,
                wordWrap: "off",
                padding: { top: 16, bottom: 16 },
                renderLineHighlight: "line",
                smoothScrolling: true,
                bracketPairColorization: { enabled: true },
                guides: { bracketPairs: true, indentation: true },
              }}
            />
            {solutionIndex >= 0 && solutionSteps[solutionIndex] && (
              <aside className="solution-guide">
                <header>
                  <span>
                    STEP {solutionIndex + 1} OF {solutionSteps.length}
                  </span>
                  <button
                    onClick={closeSolution}
                    aria-label="Close solution steps"
                  >
                    ×
                  </button>
                </header>
                <h3>{solutionSteps[solutionIndex].title}</h3>
                <p>{solutionSteps[solutionIndex].explanation}</p>
                <footer>
                  <button
                    onClick={() => goToSolutionStep(solutionIndex - 1)}
                    disabled={solutionIndex === 0}
                  >
                    ← Previous
                  </button>
                  <div>
                    {solutionSteps.map((_, index) => (
                      <i
                        key={index}
                        className={index === solutionIndex ? "active" : ""}
                      />
                    ))}
                  </div>
                  <button
                    onClick={() => goToSolutionStep(solutionIndex + 1)}
                    disabled={solutionIndex === solutionSteps.length - 1}
                  >
                    Next →
                  </button>
                </footer>
              </aside>
            )}
            {coachOn && reviewError && (
              <div className="coach-error">🔥 {reviewError}</div>
            )}
          </div>
          <div
            className="resize-handle"
            role="separator"
            aria-label="Resize output panel"
            onPointerDown={beginResize}
          >
            <span />
          </div>
          <div className="console">
            <div className="console-head">
              <span>Output</span>
              <span className="resize-hint">drag to resize</span>
            </div>
            <div className="lower-panels">
              <pre>{output}</pre>
            </div>
          </div>
        </section>
      </section>
    </main>
  );
}

export function DesktopApp() {
  return (
    <DesktopSetup>
      <AuthGate>
        <PracticeApp />
      </AuthGate>
    </DesktopSetup>
  );
}

export default function Home() {
  return <Landing />;
}

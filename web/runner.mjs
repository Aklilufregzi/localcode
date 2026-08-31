import { createServer } from 'node:http';
import { execFile } from 'node:child_process';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { promisify } from 'node:util';

const exec = promisify(execFile);
const WEB = path.dirname(new URL(import.meta.url).pathname);
const ROOT = path.resolve(WEB, '..');
const PORT = 4311;
const PROGRESS_FILE = path.join(ROOT,'.localcode-progress.json');
const testMarker = '# ---------------------------- tests ----------------------------';
const pretty = value => value.split(/[-_]/).map(word => word ? word[0].toUpperCase()+word.slice(1) : '').join(' ');

async function walk(base, extension) {
  const found = [];
  for (const topic of await fs.readdir(base, { withFileTypes:true })) {
    if (!topic.isDirectory() || topic.name.startsWith('.')) continue;
    for (const file of await fs.readdir(path.join(base, topic.name), { withFileTypes:true })) {
      if (file.isFile() && file.name.endsWith(extension) && !file.name.endsWith('.test.ts')) found.push(path.join(base, topic.name, file.name));
    }
  }
  return found;
}

async function catalog() {
  let progress={}; try{progress=JSON.parse(await fs.readFile(PROGRESS_FILE,'utf8'))}catch{}
  const map = new Map();
  const add = (file, language, base, extension) => {
    const relative = path.relative(base,file).replace(extension,'').split(path.sep).map(s=>s.replaceAll('_','-')).join('/');
    const [topic,name] = relative.split('/');
    const item = map.get(relative) ?? { id:relative, title:pretty(name), topic:pretty(topic), languages:[] };
    item.languages.push(language); map.set(relative,item);
  };
  for (const file of await walk(path.join(ROOT,'python'),'.py')) add(file,'python',path.join(ROOT,'python'),'.py');
  for (const file of await walk(path.join(ROOT,'typescript','src'),'.ts')) add(file,'typescript',path.join(ROOT,'typescript','src'),'.ts');
  return [...map.values()].map(item=>({...item,completed:Object.keys(progress[item.id]??{}).filter(language=>progress[item.id][language])})).sort((a,b)=>a.topic.localeCompare(b.topic)||a.title.localeCompare(b.title));
}

function fileFor(id,language) {
  const [topic,name] = id.split('/');
  if (!topic || !name || !/^[a-z0-9-]+$/.test(topic+name)) throw new Error('Invalid problem');
  return language==='python' ? path.join(ROOT,'python',topic.replaceAll('-','_'),`${name.replaceAll('-','_')}.py`) : path.join(ROOT,'typescript','src',topic,`${name}.ts`);
}

async function detail(id) {
  const item=(await catalog()).find(problem=>problem.id===id); if(!item) throw new Error('Problem not found');
  const code={},tests={};
  for(const language of item.languages){const file=fileFor(id,language);const full=await fs.readFile(file,'utf8');code[language]=language==='python'&&full.includes(testMarker)?full.split(testMarker)[0].trimEnd()+'\n':full; if(language==='python'){tests[language]=`${(full.match(/^def test_/gm)||[]).length} local test cases`}else{const testFile=file.replace(/\.ts$/,'.test.ts');try{const text=await fs.readFile(testFile,'utf8');tests[language]=`${(text.match(/\bit\s*\(/g)||[]).length} local test cases`}catch{tests[language]='No test file yet'}}}
  return {...item,description:`Implement ${item.title} in ${item.languages.length===2?'Python or TypeScript':pretty(item.languages[0])}. Use the local examples and edge cases to guide your solution, then run the focused test suite from this page.`,code,tests};
}

async function saveAndRun({id,language,code,action='test'}) {
  const item=(await catalog()).find(p=>p.id===id&&p.languages.includes(language)); if(!item||typeof code!=='string'||code.length>200000) throw new Error('Invalid request');
  const file=fileFor(id,language); if(language==='python'){const original=await fs.readFile(file,'utf8');const suffix=original.includes(testMarker)?original.slice(original.indexOf(testMarker)):'';await fs.writeFile(file,`${code.trimEnd()}\n\n${suffix}`)}else await fs.writeFile(file,code);
  try{
    let result;
    if(action==='run') result=language==='python' ? await exec(path.join(ROOT,'python','.venv','bin','python'),[file],{cwd:path.join(ROOT,'python'),timeout:15000,maxBuffer:1024*1024}) : await exec(path.join(ROOT,'typescript','node_modules','.bin','tsx'),[file],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024});
    else if(language==='python') result=await exec(path.join(ROOT,'python','.venv','bin','python'),['-m','pytest',file,...(action==='debug'?['-vv','--tb=long','--showlocals']:['-v'])],{cwd:path.join(ROOT,'python'),timeout:15000,maxBuffer:1024*1024});
    else {const testFile=file.replace(/\.ts$/,'.test.ts');await fs.access(testFile);result=await exec('npm',['run','test:one','--',path.relative(path.join(ROOT,'typescript'),testFile),...(action==='debug'?['--reporter=verbose']:[])],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024})}
    if(action==='submit'){let progress={};try{progress=JSON.parse(await fs.readFile(PROGRESS_FILE,'utf8'))}catch{};progress[id]={...(progress[id]??{}),[language]:true};await fs.writeFile(PROGRESS_FILE,JSON.stringify(progress,null,2)+'\n')}
    return{passed:true,submitted:action==='submit',output:`${action==='submit'?'✓ Accepted\n\n':''}${result.stdout}${result.stderr}`};
  }catch(error){return{passed:false,submitted:false,output:`${error.stdout??''}${error.stderr??''}`||error.message}}
}

const server=createServer(async(req,res)=>{res.setHeader('Access-Control-Allow-Origin','http://localhost:3000');res.setHeader('Access-Control-Allow-Headers','content-type');if(req.method==='OPTIONS'){res.writeHead(204);return res.end()}try{if(req.method==='GET'&&req.url==='/api/problems')return json(res,200,await catalog());if(req.method==='GET'&&req.url.startsWith('/api/problems/'))return json(res,200,await detail(decodeURIComponent(req.url.slice(14))));if(req.method==='POST'&&req.url==='/api/run'){let body='';for await(const chunk of req){body+=chunk;if(body.length>250000)throw new Error('Request too large')}return json(res,200,await saveAndRun(JSON.parse(body)))}json(res,404,{error:'Not found'})}catch(error){json(res,400,{error:error.message,output:error.message})}});
function json(res,status,value){res.writeHead(status,{'content-type':'application/json'});res.end(JSON.stringify(value))}
server.listen(PORT,'127.0.0.1',()=>console.log(`Local code runner: http://localhost:${PORT}`));

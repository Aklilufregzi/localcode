import { createServer } from 'node:http';
import { execFile } from 'node:child_process';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { promisify } from 'node:util';

const exec = promisify(execFile);
const WEB = path.dirname(new URL(import.meta.url).pathname);
const ROOT = process.env.LOCALQUEST_ROOT || path.resolve(WEB, '..');
const PORT = Number(process.env.LOCALQUEST_RUNNER_PORT || 4311);
const PROGRESS_FILE = path.join(ROOT,'.localcode-progress.json');
const testMarker = '# ---------------------------- tests ----------------------------';
const topicNames={'1d-dp':'1-D Dynamic Programming','2d-dp':'2-D Dynamic Programming','advanced-graphs':'Advanced Graphs','arrays-hashing':'Arrays & Hashing','binary-search':'Binary Search','bit-manipulation':'Bit Manipulation','linked-list':'Linked List','math-geometry':'Math & Geometry','sliding-window':'Sliding Window','two-pointers':'Two Pointers'};
const pretty = value => topicNames[value]??value.split(/[-_]/).map(word => word ? word[0].toUpperCase()+word.slice(1) : '').join(' ');
const canonicalTopic = value => ({one_d_dp:'1d-dp',two_d_dp:'2d-dp'}[value]??value.replaceAll('_','-'));
const canonicalName = value => value.replaceAll('_','-')==='3sum'?'three-sum':value.replaceAll('_','-');
const reviewCache = new Map();
const solutionCache = new Map();
const OLLAMA_URL=(process.env.OLLAMA_URL||'http://127.0.0.1:11434').replace(/\/$/,'');
const OLLAMA_MODEL=process.env.OLLAMA_MODEL||'qwen2.5-coder:1.5b';

async function ollamaJson(system,content,maxTokens=1600){
  let response;
  try{response=await fetch(`${OLLAMA_URL}/api/chat`,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({model:OLLAMA_MODEL,stream:false,format:'json',options:{temperature:.65,num_predict:maxTokens},messages:[{role:'system',content},{role:'user',content:system}]})})}
  catch{throw new Error('Byte is offline. Finish Local AI setup and make sure Ollama is running.')}
  const payload=await response.json().catch(()=>({}));
  if(!response.ok)throw new Error(payload.error||`Local AI failed (${response.status}).`);
  try{return JSON.parse(payload.message?.content??'')}catch{throw new Error('Byte returned an unreadable local response. Try again after your next edit.')}
}

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
    const raw = path.relative(base,file).replace(extension,'').split(path.sep); const topic=canonicalTopic(raw[0]),name=canonicalName(raw[1]); const relative=`${topic}/${name}`;
    const item = map.get(relative) ?? { id:relative, title:pretty(name), topic:pretty(topic), languages:[] };
    item.languages.push(language); map.set(relative,item);
  };
  for (const file of await walk(path.join(ROOT,'python'),'.py')) add(file,'python',path.join(ROOT,'python'),'.py');
  for (const file of await walk(path.join(ROOT,'typescript','src'),'.ts')) add(file,'typescript',path.join(ROOT,'typescript','src'),'.ts');
  const items=[...map.values()];
  await Promise.all(items.map(async item=>{try{const language=item.languages.includes('python')?'python':item.languages[0];const source=await fs.readFile(fileFor(item.id,language),'utf8');item.difficulty=metadata(source,language).difficulty}catch{item.difficulty='Practice'}}));
  const rank={Easy:0,Practice:1,Medium:2,Hard:3};
  return items.map(item=>({...item,completed:Object.keys(progress[item.id]??{}).filter(language=>progress[item.id][language])})).sort((a,b)=>a.topic.localeCompare(b.topic)||(rank[a.difficulty]??1)-(rank[b.difficulty]??1)||a.title.localeCompare(b.title));
}

function fileFor(id,language) {
  const [topic,name] = id.split('/');
  if (!topic || !name || !/^[a-z0-9-]+$/.test(topic+name)) throw new Error('Invalid problem');
  if(language==='python'){const pyTopic=({'1d-dp':'one_d_dp','2d-dp':'two_d_dp'}[topic]??topic.replaceAll('-','_'));return path.join(ROOT,'python',pyTopic,`${name.replaceAll('-','_')}.py`)}
  return path.join(ROOT,'typescript','src',topic,`${name==='three-sum'?'3sum':name}.ts`);
}

function metadata(source,language){
  const header=language==='python'?(source.match(/^"""([\s\S]*?)"""/)?.[1]??''):(source.match(/^\/\*\*([\s\S]*?)\*\//)?.[1]??'');
  const lines=header.split('\n').map(line=>line.replace(/^\s*\*?\s?/,'').trimEnd()); const titleLine=lines.find(line=>/^LeetCode\s+/i.test(line))??''; const match=titleLine.match(/^LeetCode\s+(\d+)\.\s+(.+?)\s+\((Easy|Medium|Hard)\)$/i); const url=lines.find(line=>/^https?:\/\//.test(line))??''; const urlIndex=lines.indexOf(url); const description=lines.slice(urlIndex+1).filter(line=>line&&!/^Run (just|its|everything)/i.test(line)).join(' ').replace(/\s+/g,' ').trim();
  return{number:match?.[1]??'',title:match?.[2]??'',difficulty:match?.[3]??'Practice',url,description};
}

function exampleTests(source,language){
  const examples=[];
  const friendly=value=>value.trim().replace(/\bTrue\b/g,'true').replace(/\bFalse\b/g,'false').replace(/\bNone\b/g,'null');
  const fromAssertion=(body,name)=>{const assertion=body.split('\n').map(line=>line.trim()).filter(Boolean).join(' ');const match=assertion.match(/^assert\s+(.+?)\s+(==|is|in)\s+(.+)$/);if(!match)return{name,code:body.trim().slice(0,700)};const callable=match[1].replace(/^Solution\(\)\./,'');const call=callable.match(/^[A-Za-z_]\w*\((.*)\)$/);if(!call)return{name,code:body.trim().slice(0,700)};let output=friendly(match[3]);if(match[2]==='in'&&output.startsWith('{')&&output.endsWith('}'))output=output.slice(1,-1).split(',').map(value=>value.trim()).join(' or ');return{name,input:friendly(call[1])||'No input',output}}
  if(language==='python'){const pattern=/def (test_[^(]+)\(\):\n([\s\S]*?)(?=\n\ndef test_|\n\nif __name__|$)/g;let match;while((match=pattern.exec(source))&&examples.length<5){const body=match[2].split('\n').map(line=>line.replace(/^    /,'')).join('\n').trim();examples.push(fromAssertion(body,pretty(match[1].replace(/^test_/,''))))}}
  else {const parts=source.split(/\n\s*it\(/).slice(1,6);for(const part of parts){const name=part.match(/^['"]([^'"]+)/)?.[1]??'Test case';const body=part.slice(part.indexOf('=>')+2).replace(/^\s*\{\s*/,'').replace(/\}\);[\s\S]*$/,'').trim();const flat=body.replace(/\s+/g,' ');const expectStart=flat.indexOf('expect(');const matcher=flat.match(/\)\.(?:toEqual|toBe)\(/);if(expectStart>=0&&matcher?.index!=null){const actual=flat.slice(expectStart+7,matcher.index);const call=actual.match(/^[A-Za-z_$]\w*\((.*)\)$/);const expected=flat.slice(matcher.index+matcher[0].length).replace(/\);?\s*$/,'');examples.push({name,input:friendly(call?.[1]??actual),output:friendly(expected)})}else examples.push({name,code:body.slice(0,700)})}}
  return examples;
}

async function detail(id) {
  const item=(await catalog()).find(problem=>problem.id===id); if(!item) throw new Error('Problem not found');
  const code={},tests={};let meta=null,examples=[];
  for(const language of item.languages){const file=fileFor(id,language);const full=await fs.readFile(file,'utf8');const currentMeta=metadata(full,language);if(!meta||currentMeta.description.length>meta.description.length)meta=currentMeta;code[language]=language==='python'&&full.includes(testMarker)?full.split(testMarker)[0].trimEnd()+'\n':full; if(language==='python'){tests[language]=`${(full.match(/^def test_/gm)||[]).length} local test cases`;if(!examples.length)examples=exampleTests(full,language)}else{const testFile=file.replace(/\.ts$/,'.test.ts');try{const text=await fs.readFile(testFile,'utf8');tests[language]=`${(text.match(/\bit\s*\(/g)||[]).length} local test cases`;examples=exampleTests(text,language)}catch{tests[language]='No test file yet'}}}
  return {...item,...meta,title:meta?.title||item.title,description:meta?.description||`Implement ${item.title} and make every local test pass.`,code,tests,examples};
}

async function saveAndRun({id,language,code,action='test'}) {
  const item=(await catalog()).find(p=>p.id===id&&p.languages.includes(language)); if(!item||typeof code!=='string'||code.length>200000) throw new Error('Invalid request');
  const file=fileFor(id,language); if(language==='python'){const original=await fs.readFile(file,'utf8');const suffix=original.includes(testMarker)?original.slice(original.indexOf(testMarker)):'';await fs.writeFile(file,`${code.trimEnd()}\n\n${suffix}`)}else await fs.writeFile(file,code);
  try{
    let result;
    if(action==='run'||action==='debug') {
      const debugging=action==='debug';
      result=language==='python'
        ? await exec(process.env.LOCALQUEST_PYTHON||path.join(ROOT,'python','.venv','bin','python'),[...(debugging?['-X','dev','-u']:[]),file],{cwd:path.join(ROOT,'python'),timeout:15000,maxBuffer:1024*1024,env:{...process.env,...(debugging?{PYTHONFAULTHANDLER:'1',DEBUG:'1'}:{})}})
        : process.env.LOCALQUEST_TSX
          ? await exec(process.env.LOCALQUEST_NODE||process.execPath,[process.env.LOCALQUEST_TSX,file],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024,env:{...process.env,...(debugging?{NODE_OPTIONS:`${process.env.NODE_OPTIONS??''} --enable-source-maps`.trim(),DEBUG:'1'}:{})}})
          : await exec(path.join(ROOT,'typescript','node_modules','.bin','tsx'),[file],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024,env:{...process.env,...(debugging?{NODE_OPTIONS:`${process.env.NODE_OPTIONS??''} --enable-source-maps`.trim(),DEBUG:'1'}:{})}});
    }
    else if(language==='python') result=await exec(process.env.LOCALQUEST_PYTHON||path.join(ROOT,'python','.venv','bin','python'),['-m','pytest',file,'-v'],{cwd:path.join(ROOT,'python'),timeout:15000,maxBuffer:1024*1024});
    else {const testFile=file.replace(/\.ts$/,'.test.ts');await fs.access(testFile);result=process.env.LOCALQUEST_VITEST?await exec(process.env.LOCALQUEST_NODE||process.execPath,[process.env.LOCALQUEST_VITEST,'run',testFile],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024}):await exec('npm',['run','test:one','--',path.relative(path.join(ROOT,'typescript'),testFile)],{cwd:path.join(ROOT,'typescript'),timeout:15000,maxBuffer:1024*1024})}
    if(action==='submit'){let progress={};try{progress=JSON.parse(await fs.readFile(PROGRESS_FILE,'utf8'))}catch{};progress[id]={...(progress[id]??{}),[language]:true};await fs.writeFile(PROGRESS_FILE,JSON.stringify(progress,null,2)+'\n')}
    return{passed:true,submitted:action==='submit',output:`${action==='submit'?'✓ Accepted\n\n':''}${result.stdout}${result.stderr}`};
  }catch(error){return{passed:false,submitted:false,output:`${error.stdout??''}${error.stderr??''}`||error.message}}
}

async function reviewCode({id,language,code}) {
  if (typeof code!=='string'||code.length>30000) throw new Error('Code is too large to review.');
  const item=(await catalog()).find(p=>p.id===id&&p.languages.includes(language)); if(!item) throw new Error('Invalid problem.');
  const key=`${id}:${language}:${code}`; if(reviewCache.has(key)) return reviewCache.get(key);
  const parsed=await ollamaJson(`Problem: ${item.title}\nLanguage: ${language}\n\nCode with line numbers:\n${code.split('\n').map((line,index)=>`${index+1}: ${line}`).join('\n')}`,'You are Byte, the user’s chaotic coding best friend, not a formal reviewer. Use playful roasts and tiny celebrations, never insult the person. Be technically precise and concise. Do not reveal a complete solution. Return ONLY JSON: {"summary":"...","comments":[{"line":1,"kind":"praise|roast|tip","message":"..."}]}. Line numbers must match the code.',1400);
  const result={summary:String(parsed.summary??''),comments:Array.isArray(parsed.comments)?parsed.comments.filter(c=>Number.isInteger(c.line)&&['praise','roast','tip'].includes(c.kind)).slice(0,60):[]};
  reviewCache.set(key,result); if(reviewCache.size>50)reviewCache.delete(reviewCache.keys().next().value); return result;
}

async function solutionSteps({id,language,code}) {
  const item=(await catalog()).find(p=>p.id===id&&p.languages.includes(language)); if(!item) throw new Error('Invalid problem.');
  const problem=await detail(id); const key=`${id}:${language}`; if(solutionCache.has(key)) return solutionCache.get(key);
  const parsed=await ollamaJson(`Problem: ${problem.title}\nDescription: ${problem.description}\nLanguage: ${language}\nLocal examples: ${JSON.stringify(problem.examples??[])}\nCurrent starter/attempt:\n${String(code??problem.code[language]??'').slice(0,30000)}`,'Create an accurate DSA walkthrough. Return ONLY JSON: {"steps":[{"title":"...","explanation":"...","code":"..."}]}. Produce 3 to 6 cumulative steps. Every code field is the complete runnable source at that stage and preserves the signature. Finish with the optimal solution. Keep explanations friendly and under 45 words. No Markdown fences.',5000);
  const steps=Array.isArray(parsed.steps)?parsed.steps.filter(step=>typeof step?.title==='string'&&typeof step?.explanation==='string'&&typeof step?.code==='string').slice(0,7).map(step=>({title:step.title.slice(0,100),explanation:step.explanation.slice(0,500),code:step.code.slice(0,100000)})):[];
  if(steps.length<2)throw new Error('Byte did not return enough solution steps. Try again.');
  const result={steps};solutionCache.set(key,result);if(solutionCache.size>100)solutionCache.delete(solutionCache.keys().next().value);return result;
}

const server=createServer(async(req,res)=>{const origin=req.headers.origin??'';if(/^https?:\/\/(?:localhost|127\.0\.0\.1)(?::\d+)?$/.test(origin)||origin==='tauri://localhost'||origin==='http://tauri.localhost'||origin==='https://tauri.localhost')res.setHeader('Access-Control-Allow-Origin',origin);res.setHeader('Vary','Origin');res.setHeader('Access-Control-Allow-Headers','content-type');if(req.method==='OPTIONS'){res.writeHead(204);return res.end()}try{if(req.method==='GET'&&req.url==='/api/problems')return json(res,200,await catalog());if(req.method==='GET'&&req.url.startsWith('/api/problems/'))return json(res,200,await detail(decodeURIComponent(req.url.slice(14))));if(req.method==='POST'&&['/api/run','/api/review','/api/solution'].includes(req.url)){let body='';for await(const chunk of req){body+=chunk;if(body.length>250000)throw new Error('Request too large')}const input=JSON.parse(body);return json(res,200,req.url==='/api/review'?await reviewCode(input):req.url==='/api/solution'?await solutionSteps(input):await saveAndRun(input))}json(res,404,{error:'Not found'})}catch(error){json(res,400,{error:error.message,output:error.message})}});
function json(res,status,value){res.writeHead(status,{'content-type':'application/json'});res.end(JSON.stringify(value))}
server.listen(PORT,'127.0.0.1',()=>console.log(`Local code runner: http://localhost:${PORT}`));

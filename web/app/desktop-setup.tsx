'use client';

import { useEffect, useMemo, useState } from 'react';

type SetupStep='welcome'|'python'|'ollama'|'model'|'ready'|'complete';
const steps:SetupStep[]=['welcome','python','ollama','model','ready'];

export function DesktopSetup({children}:{children:React.ReactNode}){
  const [status,setStatus]=useState<LocalQuestStatus|null>(null);
  const [step,setStep]=useState<SetupStep>('welcome');
  const [working,setWorking]=useState(false);
  const [error,setError]=useState('');
  const [setupProgress,setSetupProgress]=useState({percent:0,message:'Getting the cockpit ready…'});
  const desktop=typeof window!=='undefined'&&Boolean(window.localQuest);
  useEffect(()=>{
    if(!window.localQuest)return;
    window.localQuest.systemStatus().then(value=>{setStatus(value);if(value.pythonReady&&value.model)setStep(localStorage.getItem('localquest.onboarded')==='true'?'complete':'ready')}).catch(reason=>setError(reason.message));
    return window.localQuest.onSetupProgress(value=>setSetupProgress({percent:value.percent,message:value.message}));
  },[]);
  const index=steps.indexOf(step);
  const canContinue=useMemo(()=>step==='welcome'||step==='ready'||(step==='python'&&status?.pythonReady)||(step==='ollama'&&status?.ollama)||(step==='model'&&status?.model),[step,status]);
  if(!desktop||step==='complete')return children;
  if(step==='ready'&&status?.pythonReady&&status.model)return <ReadySlide onLaunch={()=>{localStorage.setItem('localquest.onboarded','true');setStep('complete')}}/>;
  async function run(action:'python'|'ollama'|'model'){
    setWorking(true);setError('');setSetupProgress({percent:1,message:'Starting…'});
    try{const next=action==='python'?await window.localQuest!.setupPython():action==='ollama'?await window.localQuest!.setupOllama():await window.localQuest!.setupModel();setStatus(next);setStep(action==='python'?'ollama':action==='ollama'?'model':'ready')}
    catch(reason){setError((reason as Error).message)}finally{setWorking(false)}
  }
  return <main className="setup-screen"><section className="setup-carousel"><header><div className="setup-logo">N</div><div className="setup-dots">{steps.map((name,i)=><i key={name} className={i<=index?'active':''}/>)}</div><span>{index+1} / {steps.length}</span></header><div className="setup-slide">
    {step==='welcome'&&<><span className="setup-kicker">WELCOME ABOARD</span><h1>Your coding cockpit,<br/><em>fully local.</em></h1><p>LocalQuest will prepare Python, TypeScript, and Byte on this computer. Your code never leaves the machine; only account progress syncs with Supabase.</p><div className="setup-perks"><span>⚡ Native code runs</span><span>🔥 Private AI coach</span><span>☁ Progress sync</span></div></>}
    {step==='python'&&<SetupPanel icon="⌁" kicker="STEP 1 · PYTHON" title="Prepare the Python lab" description="We’ll create an isolated environment and install pytest. Nothing is added to your project or global Python packages." ready={Boolean(status?.pythonReady)} working={working} progress={setupProgress} action="Prepare Python" onAction={()=>run('python')}/>}
    {step==='ollama'&&<SetupPanel icon="◉" kicker="STEP 2 · LOCAL AI" title="Install Byte’s engine" description="LocalQuest downloads Ollama from its official release, installs it for this user, and starts the private local service automatically." ready={Boolean(status?.ollama)} working={working} progress={setupProgress} action="Install Ollama" onAction={()=>run('ollama')}/>}
    {step==='model'&&<SetupPanel icon="🔥" kicker="STEP 3 · BYTE" title="Download Byte’s brain" description={`We’ll download ${status?.modelName||'qwen2.5-coder:1.5b'} once. It is about 1 GB and stays on this computer.`} ready={Boolean(status?.model)} working={working} progress={setupProgress} action="Download Byte" onAction={()=>run('model')}/>}
  </div>{error&&<div className="setup-error">{error}</div>}<footer><button className="setup-back" disabled={index===0||working} onClick={()=>setStep(steps[Math.max(0,index-1)])}>← Back</button>{step==='welcome'?<button className="setup-next" onClick={()=>setStep(status?.pythonReady?'ollama':'python')}>Set up LocalQuest →</button>:canContinue&&step!=='ready'?<button className="setup-next" onClick={()=>setStep(steps[index+1])}>Continue →</button>:null}</footer></section></main>
}

function SetupPanel({icon,kicker,title,description,ready,working,progress,action,onAction}:{icon:string;kicker:string;title:string;description:string;ready:boolean;working:boolean;progress:{percent:number;message:string};action:string;onAction:()=>void}){
 return <><div className="setup-hero-icon">{ready?'✓':icon}</div><span className="setup-kicker">{kicker}</span><h1>{ready?'Ready for takeoff':title}</h1><p>{ready?'This part of your local cockpit is installed and working.':description}</p>{working&&<div className="install-progress"><div><span>{progress.message}</span><b>{progress.percent}%</b></div><i><span style={{width:`${progress.percent}%`}}/></i></div>}{!ready&&!working&&<button className="setup-install" onClick={onAction}>{action}</button>}{ready&&<div className="setup-success">✓ Installed and verified locally</div>}</>
}

function ReadySlide({onLaunch}:{onLaunch:()=>void}){return <main className="setup-screen"><section className="setup-carousel setup-ready"><div className="setup-ready-mark">✓</div><span className="setup-kicker">ALL SYSTEMS GO</span><h1>LocalQuest is ready.</h1><p>Python, TypeScript, tests, and Byte are running locally. Let’s go bully some algorithms.</p><button className="setup-next" onClick={onLaunch}>Enter the quest map →</button></section></main>}

'use client';

import './landing.css';
import './landing-motion.css';
import Image from 'next/image';

const releaseBase='/downloads';

const downloads=[
  {platform:'macOS',icon:'⌘',chip:'Apple silicon',file:'LocalQuest_0.1.0_aarch64.dmg',detail:'macOS 12 or later · 86 MB installer',tone:'mac',available:true},
  {platform:'Windows',icon:'⊞',chip:'64-bit',file:'LocalQuest_0.1.0_x64-setup.exe',detail:'Windows 10 or later · 47 MB installer',tone:'win',available:true},
  {platform:'Linux',icon:'◆',chip:'Debian',file:'LocalQuest_0.1.0_amd64.deb',detail:'Ubuntu 22.04+ and Debian-based distros · 99 MB',tone:'linux',available:true},
];

export function Landing(){
  return <main className="landing">
    <nav className="landing-nav">
      <a className="landing-brand" href="#top" aria-label="LocalQuest home"><Image src="/favicon.svg" alt="" width={36} height={36}/><span>local<strong>quest</strong></span></a>
      <div><a href="#features">Features</a><a href="#downloads">Downloads</a><a className="nav-cta" href="#downloads">Get the app</a></div>
    </nav>

    <section className="landing-hero" id="top">
      <div className="hero-copy">
        <span className="eyebrow"><i/> YOUR LOCAL DSA TRAINING GROUND</span>
        <h1>Practice algorithms.<br/><em>Get roasted.</em><br/>Actually improve.</h1>
        <p>Run, debug, and submit 131 curated problems in Python and TypeScript—right on your computer. Byte, your private local AI copilot, celebrates the clean code and calls out the chaos.</p>
        <div className="hero-actions"><a className="primary-download" href={`${releaseBase}/LocalQuest_0.1.0_aarch64.dmg`} download>Download for macOS <span>↓</span></a><a href="#downloads">Other platforms</a></div>
        <div className="hero-proof"><span>✓ Code runs locally</span><span>✓ No AI API key</span><span>✓ Progress sync</span></div>
      </div>
      <div className="product-window" aria-label="LocalQuest application preview">
        <header><i/><i/><i/><b>LocalQuest</b><span>LVL 7</span></header>
        <div className="product-body">
          <aside><small>QUEST MAP</small><strong>Arrays & Hashing</strong><p className="done">★ Contains Duplicate</p><p>02 Two Sum</p><p className="locked">⌁ Group Anagrams</p><p className="locked">⌁ Top K Frequent</p></aside>
          <section><div className="mission"><small>MISSION 01 · EASY</small><h3>Contains Duplicate</h3><p>Return true if any value appears at least twice.</p></div><div className="fake-code"><div><span>1</span><code><b>export function</b> containsDuplicate(nums) &#123;</code></div><div><span>2</span><code>&nbsp; <b>const</b> seen = <b>new</b> Set();</code></div><div><span>3</span><code>&nbsp; <b>for</b> (const n of nums) &#123;</code></div><div><span>4</span><code>&nbsp;&nbsp; <mark>if (seen.has(n)) return true;</mark></code></div><div><span>5</span><code>&nbsp;&nbsp; seen.add(n);</code></div><div><span>6</span><code>&nbsp; &#125;</code></div><div><span>7</span><code>&nbsp; return false;</code></div><div><span>8</span><code>&#125;</code></div><aside>🔥 Nice. One pass, no nested-loop nonsense.</aside></div></section>
        </div>
        <footer><span>OUTPUT</span><b>✓ 4 tests passed</b><button>+100 XP</button></footer>
      </div>
    </section>

    <section className="stats"><div><strong>131</strong><span>curated problems</span></div><div><strong>2</strong><span>languages</span></div><div><strong>100%</strong><span>local execution</span></div><div><strong>0</strong><span>code sent to the cloud</span></div></section>

    <section className="feature-section" id="features">
      <div className="section-heading"><span className="eyebrow">BUILT FOR DELIBERATE PRACTICE</span><h2>A coding gym with a personality.</h2><p>Everything you need to stop passively reading solutions and start building the instincts interviews actually test.</p></div>
      <div className="feature-grid">
        <article><span>▶</span><h3>Run, debug, submit</h3><p>Explore with console output, diagnose locally, then face the complete hidden test suite.</p></article>
        <article className="orange"><span>🔥</span><h3>Byte watches your code</h3><p>Short, useful praise and playful roasts appear beside the exact lines you change.</p></article>
        <article><span>⌁</span><h3>Step-by-step solutions</h3><p>Reveal a solution one decision at a time, with cumulative code and instructor-style explanations.</p></article>
        <article><span>⚡</span><h3>Unlock the quest map</h3><p>Clear foundational problems, earn XP, and open harder challenges across every major DSA pattern.</p></article>
        <article><span>PY</span><h3>Python + TypeScript</h3><p>Switch languages per problem and exercise both skill sets with full local test coverage.</p></article>
        <article><span>◉</span><h3>Private local AI</h3><p>Ollama and Qwen power Byte on your machine. Your unfinished code stays yours.</p></article>
      </div>
    </section>

    <section className="download-section" id="downloads">
      <div className="section-heading"><span className="eyebrow">PICK YOUR PLATFORM</span><h2>Your next quest starts locally.</h2><p>The app guides you through Python, Ollama, and Byte setup on first launch.</p></div>
      <div className="download-grid">{downloads.map(item=><article key={item.platform} className={item.tone}>
        <header><span>{item.icon}</span><i>{item.chip}</i></header><h3>{item.platform}</h3><p>{item.detail}</p>{item.available?<a href={`${releaseBase}/${item.file}`} download>Download {item.platform} <span>↓</span></a>:<span className="download-unavailable">Coming soon</span>}
      </article>)}</div>
      <p className="release-note">Version 0.1.0 · Free while in preview · Ollama and the ~1 GB Byte model download during onboarding.</p>
    </section>

    <section className="local-story"><div><span className="eyebrow">LOCAL-FIRST BY DESIGN</span><h2>Your messy attempts never leave the cockpit.</h2></div><div className="flow"><span>Your code</span><b>→</b><span>Local tests</span><b>→</b><span>Local Qwen coach</span></div><p>Only account identity and completion progress sync through Supabase. Code execution, tests, debugging, and AI feedback happen on your computer.</p></section>

    <footer className="landing-footer"><a className="landing-brand" href="#top"><Image src="/favicon.svg" alt="" width={36} height={36}/><span>local<strong>quest</strong></span></a><p>Built for people who learn by breaking things locally.</p><a href="https://github.com/Aklilufregzi/localcode">GitHub ↗</a></footer>
  </main>
}

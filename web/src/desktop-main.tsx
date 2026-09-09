import React from 'react';
import { createRoot } from 'react-dom/client';
import { loader } from '@monaco-editor/react';
import * as monaco from 'monaco-editor';
import editorWorker from '../node_modules/monaco-editor/esm/vs/editor/editor.worker.js?worker';
import tsWorker from '../node_modules/monaco-editor/esm/vs/language/typescript/ts.worker.js?worker';
import { invoke } from '@tauri-apps/api/core';
import { listen } from '@tauri-apps/api/event';
import { DesktopApp } from '../app/page';
import '../app/globals.css';

self.MonacoEnvironment = {
  getWorker: (_moduleId: string, label: string) => label === 'typescript' || label === 'javascript' ? new tsWorker() : new editorWorker(),
};
loader.config({ monaco });

const browserFetch = window.fetch.bind(window);
window.fetch = async (input: RequestInfo | URL, init?: RequestInit) => {
  const url = typeof input === 'string' ? input : input instanceof URL ? input.href : input.url;
  if (!url.startsWith('http://localhost:4311') && !url.startsWith('http://127.0.0.1:4311')) return browserFetch(input, init);
  const parsed = new URL(url);
  try {
    const body = typeof init?.body === 'string' && init.body ? JSON.parse(init.body) : undefined;
    const value = await invoke<unknown>('runner_request', { method: init?.method ?? 'GET', path: `${parsed.pathname}${parsed.search}`, body });
    return new Response(JSON.stringify(value), { status: 200, headers: { 'content-type': 'application/json' } });
  } catch (error) {
    return new Response(JSON.stringify({ error: String(error), output: String(error) }), { status: 400, headers: { 'content-type': 'application/json' } });
  }
};

window.localQuest = {
  isDesktop: true,
  systemStatus: () => invoke<LocalQuestStatus>('system_status'),
  setupOllama: () => invoke<LocalQuestStatus>('setup_ollama'),
  setupPython: () => invoke<LocalQuestStatus>('setup_python'),
  setupModel: () => invoke<LocalQuestStatus>('setup_model'),
  openPythonDownload: () => invoke('open_download', { target: 'python' }),
  openOllamaDownload: () => invoke('open_download', { target: 'ollama' }),
  onSetupProgress: listener => {
    let stopped = false;
    let unlisten: (() => void) | undefined;
    listen<{ stage:string; percent:number; message:string }>('localquest:setup-progress', event => listener(event.payload))
      .then(dispose => { if (stopped) dispose(); else unlisten = dispose; });
    return () => { stopped = true; unlisten?.(); };
  },
};

createRoot(document.getElementById('root')!).render(
  <React.StrictMode><DesktopApp /></React.StrictMode>,
);

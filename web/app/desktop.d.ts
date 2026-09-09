export {};

declare global {
  type LocalQuestStatus = { python:boolean; pythonReady:boolean; typescript:boolean; ollama:boolean; model:boolean; modelName:string; workspace:string };
  interface Window {
    localQuest?: {
      isDesktop: boolean;
      systemStatus: () => Promise<LocalQuestStatus>;
      setupOllama: () => Promise<LocalQuestStatus>;
      setupPython: () => Promise<LocalQuestStatus>;
      setupModel: () => Promise<LocalQuestStatus>;
      openPythonDownload: () => Promise<void>;
      openOllamaDownload: () => Promise<void>;
      onSetupProgress: (listener:(value:{stage:string;percent:number;message:string})=>void) => () => void;
    };
  }
}

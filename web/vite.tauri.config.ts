import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  root: 'desktop',
  publicDir: '../public',
  envDir: '..',
  plugins: [react()],
  clearScreen: false,
  envPrefix: ['VITE_', 'TAURI_ENV_'],
  build: { outDir: '../dist-tauri', emptyOutDir: true },
  server: { strictPort: true },
});

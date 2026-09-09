import { copyFile, chmod, mkdir, rm } from 'node:fs/promises';
import path from 'node:path';

const runtimeDirectory = path.resolve('src-tauri/runtime');
const target = path.join(runtimeDirectory, process.platform === 'win32' ? 'node.exe' : 'node');
const obsoleteTarget = path.join(runtimeDirectory, process.platform === 'win32' ? 'node' : 'node.exe');
await mkdir(runtimeDirectory, { recursive: true });
await rm(obsoleteTarget, { force: true });
await copyFile(process.execPath, target);
if (process.platform !== 'win32') await chmod(target, 0o755);
console.log(`Prepared bundled Node runtime from ${process.execPath}`);

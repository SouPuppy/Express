const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('versions', {
  node: () => process.versions.node,
  chrome: () => process.versions.chrome,
  electron: () => process.versions.electron
})

contextBridge.exposeInMainWorld('external_addons', {
  f: () => {
    return ipcRenderer.invoke('function_f');
  },
  g: (arg1, arg2) => {
    return ipcRenderer.invoke('function_g', arg1, arg2);
  }
});

contextBridge.exposeInMainWorld('windowControls', {
  minimize: () => ipcRenderer.send('window-minimize'),
  maximize: () => ipcRenderer.send('window-maximize'),
  close:    () => ipcRenderer.send('window-close')
});
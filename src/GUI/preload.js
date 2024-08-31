window.addEventListener('DOMContentLoaded', () => {
  mainWindow.webContents.openDevTools();
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const dependency of ['chrome', 'node', 'electron']) {
      replaceText(`${dependency}-version`, process.versions[dependency])
    }
  })

const { contextBridge } = require('electron');
const addon = require('./build/Cmake/Release/addons.node');
  
contextBridge.exposeInMainWorld('myAPI', {
  mytest: () => {
    return addon.mytest();
  },
  youtest: (arg1, arg2) => {
    return addon.youtest(arg1, arg2);
  }
});
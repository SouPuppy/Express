const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('node:path')
const addons = require('../../../../build/CMake/Release/addons.node');


const createWindow = () => {
    const mainWindow = new BrowserWindow({
      width: 1000,
      height: 650,
      frame: true,
      titleBarStyle: 'hiddenInset',
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        nodeIntegration: false,
        enableRemoteModule: false,
        contextIsolation: true
      }
    });
    mainWindow.loadFile(path.join(__dirname, "../../public/index.html"));

    // mainWindow.webContents.openDevTools();
};

app.whenReady().then(() => {
  createWindow()
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
          createWindow()
    }
  })
})
  
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

ipcMain.handle('function_f', async (event) => {
  return addons.f();
});

ipcMain.handle('function_g', async (event, arg1, arg2) => {
  return addons.g(arg1, arg2);
});
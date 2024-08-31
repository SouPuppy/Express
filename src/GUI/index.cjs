const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('node:path')
const addons = require('../../build/Cmake/Release/addons.node');


app.on("ready", () => {
    const mainWindow = new BrowserWindow({
      width: 1200,
      height: 800,
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        nodeIntegration: false,
        enableRemoteModule: false,
        contextIsolation: true
      }
    });
    mainWindow.loadFile(path.join(__dirname, "public/index.html"));

    // mainWindow.webContents.openDevTools();
  });

ipcMain.handle('function_f', async (event) => {
  return addons.f();
});

ipcMain.handle('function_g', async (event, arg1, arg2) => {
  return addons.g(arg1, arg2);
});
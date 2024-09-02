const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('node:path')


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

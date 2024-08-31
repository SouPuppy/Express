const { app, BrowserWindow } = require('electron')
const path = require('node:path')

app.on("ready", () => {
    const mainWindow = new BrowserWindow({
      width: 800,
      height: 600,
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
      }
    });
    mainWindow.loadFile(path.join(__dirname, "public/index.html"));

    mainWindow.webContents.openDevTools();
  });
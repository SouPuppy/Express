const { app, BrowserWindow, ipcMain } = require('electron')
const path = require('node:path')
const addons = require('../../../../build/CMake/Release/addons.node');
let mainWindow;

const createWindow = () => {
    mainWindow = new BrowserWindow({
      width: 1000,
      height: 650,
      minWidth: 800,
      minHeight: 500,
      frame: false,
      titleBarStyle: 'hidden',
      // transparent: false,
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        nodeIntegration: false,
        contextIsolation: true,
        enableRemoteModule: true,
      }
    });
    mainWindow.loadFile(path.join(__dirname, "../../public/index.html"));
    mainWindow.setBackgroundColor('#343B48')

    mainWindow.webContents.openDevTools();
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

// ipcMain.on('window-close', () => {
//   app.close();
// });

// Handle window control events
ipcMain.on('window-close', () => {
  if (mainWindow) {
      mainWindow.close(); // Close the main window
  }
});

ipcMain.on('window-minimize', () => {
  if (mainWindow) {
      mainWindow.minimize(); // Minimize the main window
  }
});

ipcMain.on('window-maximize', () => {
  if (mainWindow) {
      if (mainWindow.isMaximized()) {
          mainWindow.unmaximize(); // Unmaximize the main window if it's maximized
      } else {
          mainWindow.maximize(); // Maximize the main window
      }
  }
});
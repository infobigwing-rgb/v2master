# Windows Portable Build Guide - Unlock Tool

## Overview
This guide creates a Windows portable version of the Unlock Tool similar to `UnlockTool_2026-04-12-0.zip`, but with the latest features including the Auto Exploit tab.

## Prerequisites (Windows System Required)
- Windows 10/11
- PowerShell (included with Windows)
- Administrator privileges (recommended)
- Internet connection for downloading dependencies

## Step-by-Step Build Process

### Step 1: Prepare the Source Code
1. Copy the entire `unlock_tool` directory to your Windows machine
2. Ensure all files are present:
   - `main.py` (main application)
   - `build_windows.spec` (PyInstaller configuration)
   - `portable_python/windows/` (portable Python environment)
   - `assets/` (UI assets)
   - `drivers/` (device drivers)
   - `platform-tools/` (ADB/Fastboot tools)

### Step 2: Install PyInstaller
Open PowerShell or Command Prompt as Administrator and navigate to the unlock_tool directory:

```powershell
cd C:\path\to\unlock_tool
.\portable_python\windows\python\python.exe -m pip install pyinstaller
```

Or using the batch file:
```cmd
build_windows.bat
```

### Step 3: Run the Build
Execute the build script:

**Option A: PowerShell (Recommended)**
```powershell
.\build_windows.ps1
```

**Option B: Command Prompt**
```cmd
build_windows.bat
```

The build process will:
- Install PyInstaller if not present
- Create `build_windows.spec` if missing
- Run PyInstaller to create the executable
- Bundle all dependencies into `dist/unlock_tool/`
- Create a portable ZIP file

### Step 4: Verify the Build
1. Check that `dist/unlock_tool/unlock_tool.exe` exists
2. Check that `unlock_tool_windows_portable_YYYY-MM-DD.zip` was created
3. Test the executable by running it:
   ```cmd
   dist\unlock_tool\unlock_tool.exe --help
   ```

### Step 5: Test the Application
1. Launch the GUI:
   ```cmd
   dist\unlock_tool\unlock_tool.exe --gui
   ```

2. Verify all tabs are present:
   - Android (10 action buttons)
   - iOS (9 action buttons)
   - Troubleshooting
   - License
   - Emergency Recovery
   - Auto Exploit (NEW)

3. Test device detection without a connected device (should show troubleshooting messages)

## Build Configuration Details

### build_windows.spec Features
- **Hidden Imports**: Includes all required modules (PyQt6, PyUSB, serial)
- **Data Files**: Bundles assets, drivers, and documentation
- **Binaries**: Includes ADB and Fastboot executables
- **Compression**: UPX compression for smaller file size
- **Windowed App**: No console window for GUI-only experience

### Portable Structure
```
unlock_tool_windows_portable_YYYY-MM-DD.zip
└── unlock_tool/
    ├── unlock_tool.exe          # Main executable
    ├── _internal/               # Bundled dependencies
    │   ├── PyQt6/              # GUI framework
    │   ├── usb/                # USB communication
    │   ├── serial/             # Serial communication
    │   ├── assets/             # UI assets (logos, badges)
    │   ├── drivers/            # Device drivers
    │   ├── platform-tools/     # ADB/Fastboot
    │   └── ...                 # Other dependencies
    └── README_Windows.md       # Windows-specific documentation
```

## Troubleshooting Build Issues

### PyInstaller Not Found
```powershell
.\portable_python\windows\python\python.exe -m pip install --upgrade pyinstaller
```

### Missing Dependencies
```powershell
.\portable_python\windows\python\python.exe -m pip install pyusb pyserial
```

### Build Fails
1. Clean previous build:
   ```cmd
   rmdir /s /q dist build
   ```

2. Reinstall PyInstaller:
   ```powershell
   .\portable_python\windows\python\python.exe -m pip uninstall pyinstaller -y
   .\portable_python\windows\python\python.exe -m pip install pyinstaller
   ```

3. Run build again

### Large File Size
- The portable version includes all dependencies (~100-150MB)
- This ensures it works on any Windows system without installation

## Distribution
1. The created ZIP file is portable and can be distributed as-is
2. Users can extract and run `unlock_tool.exe` directly
3. No installation required
4. All dependencies are bundled

## Version Naming Convention
- `unlock_tool_windows_portable_YYYY-MM-DD.zip`
- Example: `unlock_tool_windows_portable_2026-05-02.zip`

This matches the existing naming pattern while including the date for version tracking.
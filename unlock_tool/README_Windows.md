# Unlock Tool - Windows Portable Version

## Running the Application

### System Requirements
- Windows 10/11 (64-bit)
- Administrator privileges (recommended for device operations)
- USB cable that supports data transfer

### Quick Start
1. Extract the ZIP file to any folder
2. Run `unlock_tool.exe`
3. Accept the EULA when prompted
4. Connect your Android/iOS device
5. Use the appropriate tabs for device operations

### Command Line Options
```cmd
unlock_tool.exe --help          # Show help
unlock_tool.exe --gui           # Launch GUI (default)
unlock_tool.exe                 # Launch GUI
```

## Features
- **Auto Exploit Tab**: Automatically detect and run exploits for connected devices
- **Android Operations**: FRP bypass, bootloader unlock, screen lock removal, IMEI repair
- **iOS Operations**: Device management, backup/restore, passcode bypass
- **Emergency Recovery**: Advanced recovery options for bricked devices
- **Troubleshooting**: Built-in diagnostic tools and driver guidance
- **Dark Theme UI**: Modern interface with brand badges

## Device Connection Guide

### Android Devices
1. Enable USB Debugging in Developer Options
2. Connect device with USB cable
3. Allow USB debugging on device when prompted
4. Use "Detect Device" in Android tab

### iOS Devices
1. Trust the computer when prompted on device
2. Ensure iTunes or Finder is not running (may interfere)
3. Use iOS tab for device operations

### Special Modes
- **EDL Mode (Qualcomm)**: Power + Vol- while connecting USB
- **Fastboot Mode**: Power + Vol- (or specific key combo)
- **Recovery Mode**: Power + Vol+ (or specific key combo)

## Troubleshooting

### "No device detected"
- Verify USB cable supports data transfer
- Try different USB ports
- Restart device and computer
- Check Device Manager for unknown devices

### "Access denied" or permission errors
- Run as Administrator
- Install USB drivers from device manufacturer
- For Qualcomm devices: Use Zadig to install WinUSB drivers

### Application won't start
- Ensure all files were extracted from ZIP
- Check antivirus software (may flag as suspicious)
- Temporarily disable antivirus during first run

### USB communication errors
- Install Android SDK Platform Tools
- For iOS: Install iTunes or iCloud software
- Check Windows Device Manager for driver issues

## Security Notes
- This tool performs low-level device operations
- Backup important data before use
- Use at your own risk
- Some operations may void device warranty

## Support
- Check the Troubleshooting tab for diagnostic information
- Ensure device drivers are properly installed
- Verify USB connection and cable functionality

## Version Information
- Built on: 2026-05-02
- Includes latest exploit modules and UI improvements
- Portable - no installation required
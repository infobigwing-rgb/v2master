# Unlock Tool Upgrade Guide

## Overview
This upgrade adds iOS support and a license-based access control system to the existing Android unlock tool.

## Dependencies
Install the following Python packages into your virtual environment:

```bash
pip install -r requirements.txt
```

Additional iOS dependencies:
- `libimobiledevice` suite (`idevice_id`, `ideviceinfo`, `ideviceenterrecovery`, `idevicebackup2`, `idevicerestore`, `irecovery`)
- `pymobiledevice3` (optional Python bindings)

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install libimobiledevice6 libimobiledevice-utils ideviceinstaller usbmuxd libplist-utils
```

On macOS:

```bash
brew install libimobiledevice usbmuxd ideviceinstaller
```

## License Admin APK
The admin APK generates signed licenses that the desktop tool validates.

### Build steps
1. Open the Android Studio project in `ANDROID_ADMIN_APK_PROJECT.txt`.
2. Build the app and install it on a control Android device.
3. Use the app to generate license JSON strings or QR codes.

## License deployment
1. Copy the generated license Base64 string into `license.bin` in the tool root.
2. Restart the desktop app.
3. The license status is verified at startup and every 24 hours.

## iOS support
Supported hardware:
- iPhone / iPad / iPod Touch devices from 5s through 15.
- Normal, Recovery, and DFU detection via Apple VID/PID

Supported operations:
- Read device info
- Enter/exit recovery and DFU
- Backup/restore
- Erase device
- Firmware restore via `idevicerestore`
- Passcode bypass and activation lock removal stubs

## Notes
- If the tool cannot access USB devices, add udev rules on Linux via `/etc/udev/rules.d/51-android.rules`.
- On Windows, install a compatible libusb backend with Zadig.
- iOS operations rely on external tools and must be run with proper USB permissions.

# Driver Support and Device Connection Guide

This document summarizes the supported brands, connection modes, and driver guidance for the unlock tool.

## Supported Brands and Modes

- Motorola: ADB, Fastboot, Qualcomm EDL, MediaTek Preloader/BROM
- Huawei: ADB, Fastboot
- OnePlus / Nothing: ADB, Fastboot, Qualcomm EDL
- Google Pixel: ADB, Fastboot
- Samsung: ADB, Fastboot, Download Mode
- Xiaomi / Redmi / POCO: ADB, Fastboot, Qualcomm EDL
- Realme / Oppo / Vivo / iQOO: ADB, Fastboot, Qualcomm EDL
- Asus: ADB, Fastboot
- LG: ADB, Fastboot
- Nokia: ADB, Fastboot
- Sony: ADB, Fastboot
- Tecno / Infinix / Itel: ADB
- Apple iOS: Normal, Recovery, DFU
- MediaTek: Preloader, BROM
- Qualcomm: EDL

## Connection Modes

- `adb`: Android Debug Bridge; for normal Android system mode.
- `fastboot`: Bootloader mode on many Android phones.
- `qualcomm_edl`: Qualcomm Emergency Download Mode.
- `mediatek_preloader`: MediaTek Preloader mode.
- `mediatek_brom`: MediaTek BootROM mode.
- `samsung_download`: Samsung Odin/Download mode.
- `normal`, `recovery`, `dfu`: Apple iOS device modes.

## Automatic Driver Checks

Use the following helper scripts to inspect connected devices and driver readiness:

- `python scripts/driver_support_report.py`
- `python scripts/generate_udev_rules.py --output /etc/udev/rules.d/51-android.rules`

## Linux Driver Guidance

1. Install Android Platform Tools:
   - `sudo apt install android-sdk-platform-tools-common` or use the SDK package.
   - Confirm `adb version` and `fastboot version` work.
2. Install `python3-pyusb` and `libusb-1.0`.
3. Add udev rules:
   - `python scripts/generate_udev_rules.py -o /etc/udev/rules.d/51-android.rules`
   - `sudo udevadm control --reload-rules`
   - `sudo udevadm trigger`
4. Add your user to `plugdev`:
   - `sudo usermod -aG plugdev $USER`
5. Reconnect the phone and run `adb devices` / `fastboot devices`.

## Windows Driver Guidance

1. Install Android SDK Platform Tools and confirm `adb.exe`/`fastboot.exe` are available.
2. For Qualcomm EDL devices, install `Qualcomm QDLoader 9008` drivers.
3. For Samsung Download Mode, install Samsung USB/Odin drivers.
4. If a device is not recognized, use Zadig:
   - Open Zadig
   - Select the device from the list
   - Install `WinUSB` or `libusbK`
5. Use Device Manager to verify the device appears without a driver conflict.

## macOS Driver Guidance

1. Install Platform Tools via Homebrew or direct download.
2. Install `libusb` and `usbmuxd`:
   - `brew install libusb usbmuxd libimobiledevice`
3. Use `system_profiler SPUSBDataType` to verify device connections.

## Brand-Specific Notes

- Samsung devices may require `Download Mode` when the bootloader is locked.
- Qualcomm devices often require a manual EDL key combination or test-point entry.
- MediaTek phones may need a serial break or test-point to enter BROM.
- Apple devices require a supported USB cable for DFU mode.

## Reporting Best Practices

- If no device is detected, try another USB cable or port.
- On Linux, make sure the current user can access USB without `sudo`.
- On Windows, try the `Driver Support Report` script and `Device Manager`.
- Use the `Unlock Tool` UI troubleshooting tab to review log output and driver hints.

# Device Modes & Setup Guide

## Overview

The Android Servicing Tool requires your device to be in specific modes depending on the action you want to perform. This guide explains each mode and how to enter it.

## Device Modes Explained

### 1. ADB Mode (Android Debug Bridge)
**When to use**: FRP bypass, screen lock removal, basic shell operations, sideloading

**How to enter**:
1. Go to **Settings > About Phone**
2. Tap **Build Number** 7 times to enable Developer Options
3. Go to **Settings > Developer Options**
4. Enable **USB Debugging**
5. Connect device to computer via USB cable
6. A popup will appear on device - tap **Allow**

**Troubleshooting**:
- Device not detected: Try a different USB port or cable
- Permission denied: Disconnect and reconnect, then tap Allow again
- Offline: Run `adb kill-server` then `adb devices` in terminal

---

### 2. Fastboot Mode
**When to use**: Bootloader unlock/relock, bootloader operations, flashing boot/recovery

**How to enter**:
1. Enable **Developer Options** and **USB Debugging** (see ADB Mode)
2. Enable **OEM Unlock** in Developer Options (if available)
3. Power off the device completely
4. Boot into Fastboot:
   - **Most devices**: Hold **Volume Down** + **Power** button until boot menu appears
   - Select "Fastboot" or "Download Mode"
5. Connect USB cable

**For specific devices**:
- **Samsung**: May show "Download Mode" instead of "Fastboot" - same function
- **Google Pixel**: Hold **Volume Down** + **Power**
- **Xiaomi**: Hold **Volume Down** + **Power**
- **OnePlus**: Hold **Volume Down** + **Power**

**Troubleshooting**:
- Bootloader locked: Run `fastboot oem unlock` when available
- Device not detected: Install Fastboot drivers from platform-tools
- Can't hold buttons: Try `adb reboot bootloader` from ADB mode

---

### 3. EDL Mode (Emergency Download, 9008)
**When to use**: Full firmware flashing, unbricking, Qualcomm devices

**Device appears as**: "Qualcomm HS-USB QDLoader 9008" in Device Manager

**How to enter**:
1. Enable **USB Debugging** first
2. Connect device to computer
3. From ADB mode, run:
   ```bash
   adb reboot edl
   ```
4. Or manually (varies by device):
   - **Most Qualcomm**: Hold **Volume Down** + **Power** for 10+ seconds after shutdown
   - **Some Xiaomi**: Hold **Volume Down** + **Power** for 30+ seconds
   - **Some OnePlus**: Specific key combo (check device documentation)

**Troubleshooting**:
- Not appearing as 9008: 
  - Install Qualcomm drivers
  - Try different USB port
  - Ensure device has sufficient battery
- Stuck in EDL: Perform hard reset (hold Power for 30 seconds)

**Important**: EDL has lowest-level access. Be very careful!

---

### 4. Recovery Mode
**When to use**: Sideloading, factory reset, flashing recovery

**How to enter**:
1. Enable **USB Debugging**
2. Connect device and run:
   ```bash
   adb reboot recovery
   ```
3. Or manually:
   - **Most devices**: Hold **Volume Up** + **Power**
   - **Samsung**: Hold **Volume Up** + **Home** + **Power**
   - **Xiaomi**: Hold **Volume Up** + **Power**
4. Select "Apply update from ADB" or "Sideload"

**Troubleshooting**:
- Stuck in recovery: Wipe cache and factory reset (loses data!)
- Can't connect: Try entering fastboot instead and using `fastboot boot recovery.img`

---

### 5. MediaTek META Mode
**When to use**: MediaTek devices - firmware flashing, NVRAM operations

**Device appears as**: "MediaTek Preloader" in Device Manager

**How to enter**:
1. Enable **USB Debugging**
2. Connect device and run:
   ```bash
   adb reboot meta
   ```
3. Or manually (varies by device):
   - Hold **Volume Down** + **Power** for 30+ seconds
   - Some devices: **Volume Up** + **Home** + **Power**

**Troubleshooting**:
- Not detected: Install MediaTek drivers
- Reboots to Android: Try different key combination

---

### 6. Samsung Download Mode (Odin)
**When to use**: Samsung-specific firmware flashing

**How to enter**:
1. Power off device completely
2. Hold **Volume Down** + **Home** + **Power**
3. Device shows "Odin Mode" or "Download Mode"
4. Press **Volume Up** to confirm
5. Connect USB cable

**Troubleshooting**:
- Can't enter mode: Hold all buttons until mode screen appears
- Not detected: Install Samsung USB drivers

---

## Action-Specific Requirements

### FRP Bypass
- **Primary mode**: ADB
- **Backup modes**: Recovery, Fastboot
- **Steps**:
  1. Enable USB Debugging
  2. Connect in ADB mode
  3. Tool will remove Google Account verification

### Bootloader Unlock
- **Primary mode**: Fastboot
- **Prerequisite**: OEM Unlock must be enabled
- **Steps**:
  1. Enable OEM Unlock in Developer Options
  2. Reboot to Fastboot
  3. Tool will unlock bootloader
  4. Device will factory reset

### Screen Lock Removal
- **Primary mode**: ADB
- **Backup modes**: Recovery
- **Steps**:
  1. Enable USB Debugging
  2. Connect in ADB mode
  3. Tool removes lock (PIN, pattern, password)

### Firmware Flashing
- **For Qualcomm devices**: EDL mode
- **For MediaTek devices**: META mode
- **For Samsung**: Download Mode (Odin)
- **For others**: Fastboot mode
- **Prerequisite**: Have correct firmware file
- **Warning**: Can brick device if wrong firmware used!

### IMEI Repair
- **Primary mode**: EDL/META (Qualcomm/MediaTek)
- **Backup mode**: ADB (for some devices)
- **Steps**:
  1. Enter appropriate mode
  2. Tool accesses NVRAM/calibration data
  3. Repairs IMEI and network settings

### Factory Reset
- **Primary mode**: ADB or Recovery
- **Alternative**: Fastboot
- **Steps**:
  1. Connect in appropriate mode
  2. Tool wipes all data
  3. Device reboots to setup screen

---

## Troubleshooting Guide

### "Device not detected"
1. Try different USB port
2. Try different USB cable
3. Ensure correct mode enabled
4. Check drivers are installed (Windows/Mac)
5. Restart ADB: `adb kill-server` then `adb devices`

### "Permission denied"
1. Disconnect device
2. Reconnect and tap "Allow" on device screen
3. Or reconnect and try again

### "Device offline"
1. Unplug USB cable
2. Reconnect and wait 2-3 seconds
3. Run `adb devices` again

### "Bootloader locked"
1. Enable OEM Unlock in Developer Options
2. Reboot to Fastboot
3. Run `fastboot oem unlock`
4. Confirm on device

### "Can't enter EDL mode"
1. Ensure USB Debugging is enabled first
2. Try `adb reboot edl` command
3. If stuck: Hard reset (hold Power 30+ seconds)
4. Try different USB port

### "Driver not found (Windows)"
1. Install platform-tools drivers
2. Or right-click device in Device Manager > Update Driver
3. Select "Browse" and choose driver folder

---

## Quick Reference

| Action | Mode | Keys | ADB Command |
|--------|------|------|-------------|
| FRP Bypass | ADB | USB Debug | - |
| Bootloader Unlock | Fastboot | Vol Down + Power | `adb reboot bootloader` |
| Screen Lock Remove | ADB | USB Debug | - |
| Firmware Flash | EDL/META | Device specific | `adb reboot edl` / `adb reboot meta` |
| IMEI Repair | EDL/META | Device specific | `adb reboot edl` / `adb reboot meta` |
| Factory Reset | ADB/Recovery | USB Debug / Vol Up + Power | `adb reboot recovery` |

---

## Safety Tips

✓ **DO**:
- Read guides for your specific device
- Backup important data first
- Use original USB cable
- Keep device plugged in during flashing
- Follow steps in order
- Use correct firmware for your device

✗ **DON'T**:
- Use random firmware files
- Disconnect device during operations
- Turn off device during flashing
- Use damaged or cheap USB cables
- Flash multiple devices simultaneously
- Panic if something goes wrong!

---

## Still Having Issues?

1. Check the "Device Guides" tab in the tool
2. Read the mode-specific guides above
3. Ensure you're using the latest platform-tools
4. Try a different USB port or cable
5. Check device manufacturer support forums
6. Ensure device battery is above 50%

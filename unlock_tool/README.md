# Android Servicing Tool

A comprehensive, production-ready Android device servicing tool supporting all modern devices and the latest exploitation methods as of 2026.

## Features

### Core Features
- **FRP (Google Account) Bypass** - Support for Android 5.0 through 16
- **Bootloader Unlock/Relock** - Including locked OEM, Samsung VaultKeeper, Xiaomi HyperOS restrictions
- **Firmware Flashing & Repair** - Full flashing, partial flashing, OTA update injection
- **Screen Lock Removal** - PIN, Pattern, Password, Face Unlock, Fingerprint (with secure element bypass)
- **IMEI Repair & Network Fix** - Certificate injection, QCN repair, modem reinitialization
- **Factory Reset** - With/without data backup option
- **Security Bypass** - Knox, TEE, dm-verity, AVB 2.0, vbmeta

### Supported Platforms
- **Qualcomm** - EDL 9008 mode, Firehose loaders for all chipsets
- **MediaTek** - BootROM, Preloader, META mode, Download Agent
- **Samsung** - Exynos, Snapdragon with Knox bypass
- **Google Tensor** - Pixel 6-10, Pixel Fold series
- **Huawei/Honor** - Kirin chipsets, HarmonyOS
- **Apple** - iOS 15-19 (limited passcode bypass)

### Device Support
- Samsung Galaxy S/A/M/Z/F series (2022-2026)
- Xiaomi Mi/Redmi/POCO/HyperOS devices (2023-2026)
- Oppo/OnePlus/Realme ColorOS/OxygenOS (2023-2026)
- Vivo/iQOO FuntouchOS/OriginOS (2023-2026)
- Google Pixel 6-10, Pixel Fold (2021-2026)
- Motorola Moto G/E/Edge (2022-2026)
- Nothing Phone 1/2/3 (2023-2026)
- Honor Magic/X series (2023-2026)
- Tecno/Infinix/Itel latest models (2024-2026)
- ASUS ROG/Zenfone

## Installation

### Requirements
- Python 3.11+
- Windows 10/11, macOS 12+, Ubuntu 22.04+
- USB drivers for target platforms

### Setup
```bash
git clone <repository>
cd unlock_tool
pip install -r requirements.txt
```

### Drivers Installation
Run the appropriate driver installer:
- Windows: `drivers/windows/install-windows-drivers.bat`
- Linux: `drivers/linux/install-linux-edl-drivers.sh`
- macOS: `drivers/mac/install-macos-drivers.sh`

### Packaging and Distribution
The tool includes packaging metadata for Python installation and distribution:
- `pyproject.toml` for build metadata and dependencies
- `MANIFEST.in` for source distribution file inclusion
- `run-portable.sh` for portable Linux startup
- `run-portable.bat` for portable Windows startup

## Usage

### GUI Mode (Recommended)
```bash
python main.py --gui
```

### CLI Mode (Advanced)
```bash
python main.py --cli --device auto --action frp_bypass
```

### Available Actions
- `frp_bypass` - Remove Google account verification
- `bootloader_unlock` - Unlock device bootloader
- `screen_lock_remove` - Remove screen locks
- `firmware_flash` - Flash firmware images
- `imei_repair` - Repair IMEI and network
- `factory_reset` - Factory reset device

## Project Structure

```
unlock_tool/
├── main.py                 # Entry point with GUI/CLI selector
├── core/                   # Core communication and detection
│   ├── usb_manager.py      # Low-level USB communication
│   ├── device_detector.py  # Auto-detect devices
│   ├── adb_interface.py    # ADB protocol implementation
│   ├── fastboot_interface.py # Fastboot protocol
│   └── logger.py           # Logging system
├── modules/                # Exploitation modules
│   ├── frp/                # FRP bypass methods
│   ├── unlock/             # Bootloader/screen unlock
│   ├── flash/              # Firmware flashing
│   ├── imei/               # IMEI repair
│   └── utils/              # Utility functions
├── drivers/                # Platform-specific drivers
├── payloads/               # Pre-compiled exploits
├── database/               # Device database
├── gui/                    # GUI components
└── requirements.txt        # Python dependencies
```

## Safety & Legal

⚠️ **DISCLAIMER**: This tool is for educational purposes only. Use only on devices you own or have explicit permission to service. The developers are not responsible for bricked devices, data loss, or legal consequences.

### Safety Features
- Automatic backup creation before modifications
- Brick prevention rollback mechanisms
- Ownership verification checks
- Detailed logging for troubleshooting

## Development

### Adding New Devices
1. Add device profile to `database/devices.json`
2. Implement brand-specific modules if needed
3. Test on physical device
4. Update documentation

### Contributing
1. Fork the repository
2. Create feature branch
3. Add tests and documentation
4. Submit pull request

## License

MIT License - See LICENSE file for details.

## Version

2.0.0 (2026)
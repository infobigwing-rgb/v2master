# Installation and Device Connection Guide

This guide explains how to connect devices successfully to the project, including portable usage, Windows installer packaging, driver setup for Linux, and required module verification.

## 1. Portable Version (Recommended)

The portable version now includes bundled Python interpreters for true plug-and-play usage on any compatible PC.

### Cross-Platform Portable Setup

1. Copy the entire `unlock_tool/` folder to your USB drive or any writable location.

2. Run the setup script for your operating system (only needed once):
   - **Linux/macOS:** `./setup.sh`
   - **Windows:** `setup.bat`

   This installs all Python dependencies into the bundled portable Python.

3. Install drivers (required on each PC):
   - **Linux:** `sudo bash drivers/linux/install-linux-edl-drivers.sh`
   - **Windows:** `drivers\windows\install-windows-drivers.bat` then install appropriate drivers
   - **macOS:** Follow guidance in `drivers/mac/install-macos-drivers.sh`

4. Run the tool:
   - **Linux/macOS:** `./run.sh --gui`
   - **Windows:** `run.bat --gui`

### What makes it portable?

- **Bundled Python:** No need to install Python 3.11+ on the target PC
- **Pre-installed dependencies:** All required packages are included
- **Platform-specific binaries:** Separate Python builds for Windows, Linux, and macOS
- **Self-contained:** Everything runs from the folder, no system modifications beyond drivers

## 2. Windows Install Package

For a single-package Windows installer, use the existing `install_edl_win10_win11.ps1` script as a template and include the following in the package:

- Python 3.9+ or Python 3.11 installer
- Git client
- `zadig` or USB driver installer
- The project sources
- A PowerShell install script that:
  - installs Python and Git when missing
  - clones or copies the repo
  - installs dependencies via `python -m pip install -r requirements.txt`
  - adds the project folder to `PATH`
  - prompts the user to run `zadig` for WinUSB driver installation

### Suggested Windows install flow

1. Run the installer package or `install_edl_win10_win11.ps1`.
2. Install `Python` and `Git` if missing.
3. Install required drivers using `zadig` for Qualcomm and ADB devices.
4. Add the unpacked tool folder to system `PATH`.
5. Launch `python main.py --gui` from the installer environment.

### Driver notes for Windows

- Use `zadig` to install WinUSB for Qualcomm EDL devices.
- For QHSUSB_BULK devices, install the driver only after the phone is connected.
- If the phone appears with a Yellow warning icon in Device Manager, reinstall using `zadig`.

## 3. Linux Driver Setup

The repository includes Linux driver files under `/home/tjms/Downloads/edl-master/Drivers`.

### Use the provided Linux installer

1. Run the udev/driver script as root:
   ```bash
   cd /home/tjms/Downloads/edl-master
   sudo bash ./install-linux-edl-drivers.sh
   ```

2. That script copies:
   - `Drivers/50-android.rules`
   - `Drivers/51-edl.rules`
   - `Drivers/69-libmtp.rules`
   - `Drivers/blacklist-qcserial.conf`

3. Reload udev rules:
   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

4. If you are on a systemd-based distro, stop ModemManager:
   ```bash
   sudo systemctl stop ModemManager
   sudo systemctl disable ModemManager
   ```

5. Reboot if required.

### Optional full Linux install

Use the provided autoinstall script to install drivers and Python dependencies:

```bash
cd /home/tjms/Downloads/edl-master
sudo ./autoinstall.sh
```

This will:
- install Linux drivers
- install the Python dependencies from `requirements.txt`
- install the project into the system Python environment

## 4. Device Connection Checklist

### A. USB mode and detection

- For Android/ADB: connect the device and enable USB debugging.
- For Fastboot: reboot the phone to bootloader/fastboot mode.
- For Qualcomm EDL: boot the device into EDL mode (USB PID `0x9008`).

### B. Confirm the device is visible

Linux:
```bash
adb devices
fastboot devices
lsusb | grep -i qualcomm
```

Windows:
```powershell
adb devices
fastboot devices
```

### C. If the device is not detected

- Ensure the correct driver is installed:
  - Linux: udev rules, disable ModemManager
  - Windows: install WinUSB for the device with `zadig`
- Check physical USB cable and port.
- Use a dedicated USB 2.0 port when possible.
- On Qualcomm phones, use an EDL cable or button combo to force 9008 mode.

### D. Specific connection notes for this project

- `unlock_tool` currently detects devices via ADB/Fastboot/USB enumeration.
- If using `edl-master`, the device must be in Qualcomm EDL mode or provide a serial interface.
- For Qualcomm EDL, the tool expects the USB PID to be `0x9008`.

## 5. Required Modules and Dependency Check

### unlock_tool required Python modules

Install with:
```bash
python3 -m pip install -r /home/tjms/Downloads/v2master/unlock_tool/requirements.txt
```

Key packages include:
- `PyQt6`
- `pyusb`
- `pyserial`
- `adb-shell`
- `fastboot-tools`
- `cryptography`
- `requests`
- `lxml`
- `colorama`
- `tqdm`
- `pyyaml`
- `jsonschema`
- `psutil`
- `platformdirs`
- `packaging`

### edl-master required Python modules

Install with:
```bash
python3 -m pip install -r /home/tjms/Downloads/edl-master/requirements.txt
```

Key packages include:
- `wheel`
- `pyusb`
- `pyserial`
- `docopt`
- `pycryptodome`
- `pycryptodomex`
- `lxml`
- `colorama`
- `capstone`
- `keystone-engine`
- `qrcode`
- `requests`
- `passlib`
- `Exscript`

### Verify installation

Run:
```bash
python3 -m pip check
python3 -c "import usb, serial, lxml, requests, qrcode, passlib, capstone, keystone" || echo 'Missing modules'
```

### Windows module check

Open PowerShell in the activated venv and run:
```powershell
python -m pip install -r .\requirements.txt
python -m pip list
```

## 6. Portable vs Installed Workflow

### Portable workflow

- Use the extracted folder directly.
- Keep the `.venv` directory inside the project.
- Do not require system-wide Python or admin rights for the tool itself.
- Ideal for quick deployment.

### Installed workflow

- Use the Windows installer script or Linux autoinstall script.
- Install required drivers and dependencies system-wide.
- Suitable for a single machine service workstation.

## 7. Recommended Windows distribution strategy

For a true single-package Windows release, bundle:
- the project folder
- a Python embeddable runtime or installer script
- `install_edl_win10_win11.ps1`
- a `drivers/` subfolder containing `zadig` instructions
- a simple launcher script

The launch process should:
1. install Python if missing,
2. install Git if missing,
3. install Python dependencies,
4. guide the user to install drivers via `zadig`,
5. start `main.py --gui`.

## 8. Troubleshooting

### Common issues

- `ModuleNotFoundError`: activate `.venv` and reinstall requirements.
- `No module named 'PyQt6'`: install `PyQt6` in the active environment.
- USB detection fails: install correct driver and rerun `udevadm` on Linux.
- `adb` or `fastboot` not found: install Android platform tools and ensure they are on `PATH`.

### Useful commands

Linux:
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
adb kill-server
adb start-server
```

Windows:
```powershell
python -m pip install -r requirements.txt
adb devices
fastboot devices
```

## Portable Startup

Linux portable startup:
```bash
./run-portable.sh
```

Windows portable startup:
```powershell
run-portable.bat
```

## Packaging Files

This repository now includes packaging metadata files for Python distribution and installation:
- `pyproject.toml`
- `MANIFEST.in`
- `README.md`
- `INSTALLATION.md`

These files make the tool ready for source packaging, wheel distribution, and portable deployment.

## EDL Tool Integration

The `v2master` folder includes a copy of the existing EDL tools under `Tools/` and the Linux driver rules under `Drivers/`.

- `Tools/` contains the original `edl-master` utility scripts such as `enableadb.py`, `qc_diag.py`, `sierrakeygen.py`, `fhloaderparse.py`, and the legacy EDL library.
- `Drivers/` contains `udev` rules and driver configuration files required for Linux device detection and access.

For Linux, use the copied driver rules from `Drivers/` with:
```bash
sudo cp Drivers/*.rules /etc/udev/rules.d/
sudo cp Drivers/blacklist*.conf /etc/modprobe.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
```

For Windows, use the provided `Tools/Windows/Install_Windows.bat` and the PowerShell installer script template from the original EDL repository.

---

This guide is designed to make the tool portable, to support a Windows single-package installer model, and to ensure the necessary modules and drivers are checked using the existing `/home/tjms/Downloads/edl-master` resources.

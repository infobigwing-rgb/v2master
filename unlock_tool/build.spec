# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules

ROOT_DIR = Path(os.getcwd()).resolve()

binaries = []
datas = [
    (str(ROOT_DIR / 'devices.json'), '.'),
    (str(ROOT_DIR / 'drivers'), 'drivers'),
    (str(ROOT_DIR / 'assets'), 'assets'),
    (str(ROOT_DIR / 'README.md'), '.'),
    (str(ROOT_DIR / 'EULA.txt'), '.'),
]

project_specific = ROOT_DIR / 'platform-tools'
if project_specific.exists():
    datas.append((str(project_specific), 'platform-tools'))

if sys.platform == 'win32':
    adb = ROOT_DIR / 'platform-tools' / 'adb.exe'
    fastboot = ROOT_DIR / 'platform-tools' / 'fastboot.exe'
    if adb.exists():
        binaries.append((str(adb), '.'))
    if fastboot.exists():
        binaries.append((str(fastboot), '.'))
    libs = ROOT_DIR / 'drivers' / 'windows'
    if libs.exists():
        datas.append((str(libs), 'drivers/windows'))
elif sys.platform == 'darwin':
    for tool in ['ideviceinfo', 'idevicerestore', 'idevicebackup2', 'ideviceenterrecovery', 'irecovery', 'checkra1n']:
        path = ROOT_DIR / 'tools' / tool
        if path.exists():
            binaries.append((str(path), '.'))
    datas.append((str(ROOT_DIR / 'drivers'), 'drivers'))
else:
    for tool in ['adb', 'fastboot']:
        path = ROOT_DIR / 'platform-tools' / tool
        if path.exists():
            binaries.append((str(path), '.'))
    for tool in ['ideviceinfo', 'idevicerestore', 'idevicebackup2', 'ideviceenterrecovery', 'irecovery', 'checkra1n']:
        path = ROOT_DIR / 'tools' / tool
        if path.exists():
            binaries.append((str(path), '.'))
    datas.append((str(ROOT_DIR / 'drivers'), 'drivers'))

hidden_imports = collect_submodules('modules')

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[str(ROOT_DIR)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe_name = 'unlock_tool.exe' if sys.platform == 'win32' else 'unlock_tool'
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='unlock_tool',
)

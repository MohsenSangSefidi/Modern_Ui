# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/Game/Desktop/Modern Ui Design/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Game/Desktop/Modern Ui Design/resources', 'resources/'), ('C:/Users/Game/Desktop/Modern Ui Design/logs', 'logs/'), ('C:/Users/Game/Desktop/Modern Ui Design/interface.ui', '.'), ('C:/Users/Game/Desktop/Modern Ui Design/resources.qrc', '.'), ('C:/Users/Game/Desktop/Modern Ui Design/resources_rc.py', '.'), ('C:/Users/Game/Desktop/Modern Ui Design/style.json', '.'), ('C:/Users/Game/Desktop/Modern Ui Design/ui_interface.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Game\\Desktop\\Modern Ui Design\\logo.ico'],
)

# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

collect = []

scripts = [
    'ncrar-abr.py', 
    'ncrar-abr-gui.py', 
    'ncrar-abr-aggregate.py',
    'ncrar-abr-batch.py', 
    'ncrar-abr-compare.py'
]


exclude_binaries = TOC([
    ('Qt6WebEngineCore.dll', None, None),
    ('libopenblas64__v0.3.23-246-g3d31191b-gcc_10_3_0.dll', None, None),
    ('libopenblas_v0.3.20-571-g3dec11c6-gcc_10_3_0-c2315440d6b6cef5037bad648efc8c59.dll', None, None),
])


for script in scripts:
	a = Analysis(
		[f'scripts/{script}'],
		pathex=[],
		binaries=[],
		datas=[],
		hiddenimports=[],
		hookspath=['hooks'],
		hooksconfig={},
		runtime_hooks=[],
		excludes=[],
		win_no_prefer_redirects=False,
		win_private_assemblies=False,
		cipher=block_cipher,
		noarchive=False,
	)
    #a.binaries = a.binaries - exclude_binaries

	pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
	exe = EXE(
		pyz,
		a.scripts,
		[],
		exclude_binaries=True,
		name=script[:-3],
		debug=False,
		bootloader_ignore_signals=False,
		strip=False,
		upx=True,
		console=True,
		disable_windowed_traceback=False,
		argv_emulation=False,
		target_arch=None,
		codesign_identity=None,
		entitlements_file=None,
	)

	collect.append(a.binaries)
	collect.append(a.zipfiles)
	collect.append(a.datas)
	collect.append(exe)

coll = COLLECT(
	*collect, 
	strip=False,
	upx=True,
	upx_exclude=[],
	name='ncrar-abr',
)

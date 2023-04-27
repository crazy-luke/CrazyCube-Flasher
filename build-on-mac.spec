# -*- mode: python -*-

block_cipher = None

a = Analysis(['nodemcu-pyflasher.py'],
             binaries=None,
             datas=[("images", "images")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CrazyCube Flasher',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='images/icon.png')
app = BUNDLE(exe,
             name='CrazyCube Flasher.app',
             version='1.0.0',
             icon='./images/icon.png',
             bundle_identifier='com.frightanic.nodemcu-pyflasher')

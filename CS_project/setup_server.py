# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('server.py', targetName='chat_server.exe')]

excludes = ['unit_tests', 'client']

includes = ['logging', 'socket', 'sqlalchemy', 'hmac', 'hashlib', 'binascii', 'threading', 'time', 'PyQt5']

zip_include_packages = ['server', 'common', 'logs', 'socket', 'sqlalchemy',
                        'hmac', 'hashlib', 'binascii', 'threading', 'time', 'PyQt5']

options = {
    'build_exe': {
        'include_msvcr': True,
        'excludes': excludes,
        'includes': includes,
        'zip_include_packages': zip_include_packages,
        'build_exe': 'build_windows_server',
    }
}

setup(name='PyQt ChatApp',
      version='0.1.0',
      description='Simple chat server app',
      executables=executables,
      options=options)

from distutils.core import setup, Extension
import os

ch_exts = [os.path.join('src', name) for name in os.listdir('src')
           if name.endswith('.c')]

ch_module = Extension('charlockholmes',
                      ch_exts)

setup (name = 'charlockholmes',
       version = '1.0',
       description = 'Character encoding detecting library for Python using ICU and libmagic.',
       ext_modules = [ch_module])

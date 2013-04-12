from distutils.core import setup, Extension

ch_module = Extension('charlockholmes',
                      sources = ['charlockholmes.c'])

setup (name = 'charlockholmes',
       version = '1.0',
       description = 'Character encoding detecting library for Python using ICU and libmagic.',
       ext_modules = [ch_module])

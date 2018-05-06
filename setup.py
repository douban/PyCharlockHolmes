from setuptools import setup, Extension, find_packages
import os
from os import path

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Use environment variable ICUI18N to set your own icui18n configuration.
icui18n_path = os.getenv("ICUI18N")
if icui18n_path is None:
        icui18n_path = '/usr/local'

icui18n_bin = os.path.join(icui18n_path, 'bin')
icui18n_include = os.path.join(icui18n_path, 'include')
icui18n_lib = os.getenv('ICUI18N_LIB', os.path.join(icui18n_path, 'lib'))

magic_path = os.getenv("MAGIC")
if magic_path is None:
        magic_path = '/usr/local'
magic_bin = os.path.join(magic_path, 'bin')
magic_include = os.path.join(magic_path, 'include')
magic_lib = os.getenv('MAGIC_LIB', os.path.join(magic_path, 'lib'))

# os.system('cd ./lib; ./build.sh')

ch_exts = [
    os.path.join('src', name) for name in os.listdir('src')
    if name.endswith('.c')
]

# ch_module = Extension('charlockholmes', ch_exts, include_dirs=['./lib/magic/include'], library_dirs=['./lib/magic/lib'], libraries=['icui18n'])
ch_module = Extension('charlockholmes',
                      ch_exts,
                      include_dirs=[icui18n_include, magic_include],
                      library_dirs=[icui18n_lib, magic_lib],
                      libraries=['icui18n', 'magic'])

setup (
    name='charlockholmes',
    version='0.0.3',
    description='Character encoding detecting library for Python using ICU and libmagic.',
    long_description=long_description,
    url='https://github.com/douban/PyCharlockHolmes',
    ext_modules=[ch_module],
    keywords=['icu', 'magic', 'charlockholmes', 'egg'],
    license='Modified BSD License',
    author='xtao',
    author_email='xutao881001@gmail.com',
)

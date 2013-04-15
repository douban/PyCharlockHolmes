from distutils.core import setup, Extension
import os

# os.system('cd ./lib; ./build.sh')

ch_exts = [
    os.path.join('src', name) for name in os.listdir('src')
    if name.endswith('.c')
]

# ch_module = Extension('charlockholmes', ch_exts, include_dirs=['./lib/magic/include'], library_dirs=['./lib/magic/lib'], libraries=['icui18n'])
ch_module = Extension('charlockholmes', ch_exts, libraries=['icui18n', 'magic'])

setup (
    name='charlockholmes',
    version='0.0.1',
    description='Character encoding detecting library for Python using ICU and libmagic.',
    ext_modules=[ch_module],
    keywords=('icu', 'magic', 'charlockholmes', 'egg'),
    license='MIT License',
    author='xtao',
    author_email='xutao881001@gmail.com',
)

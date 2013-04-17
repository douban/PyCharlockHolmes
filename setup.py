from distutils.core import setup, Extension
import os

# Use environment variable ICUI18N to set your own icui18n configuration.
icui18n_path = os.getenv("ICUI18N")
if icui18n_path is None:
    if os.name == 'nt':
        program_files = os.getenv("ProgramFiles")
        icui18n_path = '%s\icui18n' % program_files
    else:
        icui18n_path = '/usr/local'

icui18n_bin = os.path.join(icui18n_path, 'bin')
icui18n_include = os.path.join(icui18n_path, 'include')
icui18n_lib = os.getenv('ICUI18N_LIB', os.path.join(icui18n_path, 'lib'))

# os.system('cd ./lib; ./build.sh')

ch_exts = [
    os.path.join('src', name) for name in os.listdir('src')
    if name.endswith('.c')
]

# ch_module = Extension('charlockholmes', ch_exts, include_dirs=['./lib/magic/include'], library_dirs=['./lib/magic/lib'], libraries=['icui18n'])
ch_module = Extension('charlockholmes',
                      ch_exts,
                      include_dirs=[icui18n_include, 'include'],
                      library_dirs=[icui18n_lib],
                      libraries=['icui18n', 'magic'])

setup (
    name='charlockholmes',
    version='0.0.1',
    description='Character encoding detecting library for Python using ICU and libmagic.',
    url='https://github.com/xtao/PyCharlockHolmes',
    ext_modules=[ch_module],
    keywords=('icu', 'magic', 'charlockholmes', 'egg'),
    license='BSD License',
    author='xtao',
    author_email='xutao881001@gmail.com',
)

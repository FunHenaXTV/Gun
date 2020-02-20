from distutils.core import setup, Extension, DEBUG

sfc_module = Extension('computation', sources = ['computation.cpp'])

setup(name = 'computation', version = '1.0',
    description = 'Python Package with superfastcode C++ extension',
    ext_modules = [sfc_module]
    )


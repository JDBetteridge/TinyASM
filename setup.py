import os
import petsc4py

from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

petsc = petsc4py.get_config()
petsc_path = petsc_lib = os.path.join(
    petsc4py.get_config()['PETSC_DIR'],
    petsc4py.get_config()['PETSC_ARCH']
)
petsc_include = os.path.join(petsc_path, 'include')
petsc_library = os.path.join(petsc_path, 'lib')

ext_modules = [
    Pybind11Extension(
        name="tinyasm._tinyasm",
        sources=sorted(glob("tinyasm/*.cpp")),  # Sort source files for reproducibility
        include_dirs=[petsc_include, petsc4py.get_include()],
        library_dirs=[petsc_library],
        extra_link_args=['-lpetsc',],
        runtime_library_dirs=[petsc_library],
    ),
]

description = r'''
The goal of this is to give a) fast performance for small local patches and b)
provide a playground for experimenting with new patch features that does not
require digging deep into PETSc.
'''

setup(
    name='tinyasm',
    version='0.0.1',
    author='Florian Wechsung',
    author_email='wechsung@nyu.edu',
    description='A tiny implementation of PETSc PCASM.',
    long_description=description,
    install_requires=['pybind11'],
    packages=['tinyasm'],
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)

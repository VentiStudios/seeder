from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["main_cython.py", "main_optimized.py"]))
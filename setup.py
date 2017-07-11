#!/usr/bin/env python

from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

import base62


cython_extensions = [
    Extension('base62', ['base62.py']),
]


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        return '(Could not read from README.rst)'


setup(name='pybase62',
      py_modules=['base62'],
      ext_modules=cythonize(cython_extensions),
      version=base62.__version__,
      description='Python module for base62 encoding',
      long_description=readme(),
      author='Sumin Byeon',
      author_email='suminb@gmail.com',
      url='http://github.com/suminb/base62',
      packages=[],
      )

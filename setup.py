#!/usr/bin/env python

from distutils.core import setup
import base62


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        return '(Could not read from README.rst)'


setup(name='pybase62',
      py_modules=['base62'],
      version=base62.__version__,
      description='Python module for base62 encoding',
      long_description=readme(),
      author='Sumin Byeon',
      author_email='suminb@gmail.com',
      url='http://github.com/suminb/base62',
      packages=[],
     )

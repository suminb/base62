[![Build Status](https://travis-ci.org/suminb/base62.svg?branch=master)](https://travis-ci.org/suminb/base62)

A Python module for base62 encoding. Ported from PHP code that I wrote in mid-2000, which can be found on [here](http://blog.suminb.com/archives/558).

## Installation

[![PyPI](https://img.shields.io/pypi/v/pybase62.svg)](https://pypi.python.org/pypi/pybase62)

```
pip install pybase62
```

## Usage

```python
>>> import base62

>>> base62.encode(34441886726)
'base62'

>>> base62.decode('base62')
34441886726
```

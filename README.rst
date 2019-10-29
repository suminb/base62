base62
======

|Build Status| |Coveralls| |PyPI|

A Python module for ``base62`` encoding. Ported from PHP code that I wrote
in mid-2000, which can be found
`here <http://philosophical.one/posts/base62>`__.

.. |Build Status| image:: https://travis-ci.org/suminb/base62.svg?branch=master
   :target: https://travis-ci.org/suminb/base62
.. |PyPI| image:: https://img.shields.io/pypi/v/pybase62.svg
   :target: https://pypi.python.org/pypi/pybase62
.. |Coveralls| image:: https://coveralls.io/repos/github/suminb/base62/badge.svg?branch=master
   :target: https://coveralls.io/github/suminb/base62?branch=develop


Rationale
---------

When writing a web application, often times we would like to keep the URLs
short.

::

    http://localhost/posts/V1Biicwt

This certainly gives a more concise look than the following.

::

    http://localhost/posts/109237591284123

This was the original motivation to write this module, but there shall be much
more broader potential use cases of this module. The main advantage of
``base62`` is that it is URL-safe (as opposed to ``base64``) due to the lack of
special characters such as '``/``' or '``=``'. Another key aspect is that the
alphabetical orders of the original (unencoded) data is preserved when encoded.
In other words, encoded data can be sorted without being decoded at all.

Installation
============

``base62`` can be installed via ``pypi``. Unfortunately, the package name
``base62`` on ``pypi`` had already been occupied by someone else, so we had to
go by ``pybase62``.

::

    pip install pybase62

Alternatively, you may clone the code to manually install it.

::

    git clone https://github.com/suminb/base62
    cd base62 && python setup.py install

Usage
=====

The following section describes a basic usage of ``base62``.

.. code:: python

    >>> import base62

    >>> base62.encode(34441886726)
    'base62'

    >>> base62.decode('base62')
    34441886726

From version ``0.2.0``, ``base62`` supports ``bytes`` array encoding as well.

.. code:: python

    >>> base62.encodebytes(b'\0')
    0

    >>> base62.encodebytes(b'\xff\xff')
    H31

    >>> base62.decodebytes('0')
    b''

    >>> base62.decodebytes('1')
    b'\x01'

Some may be inclined to assume that they both take ``bytes`` types as input
due to their namings. However, ``encodebytes()`` takes ``bytes`` types
whereas ``decodebytes()`` takes ``str`` types as an input. They are intended
to be commutative, so that a *roundtrip* between both functions yields the
original value.

Formally speaking, we say function *f* and *g* commute if *f∘g* = *g∘f* where
*f(g(x))* = *(f∘g)(x)*.

Therefore, we may expect the following relationships:

* ``value == encodebytes(decodebytes(value))``
* ``value == decodebytes(encodebytes(value))``

Tests
=====

You may run some test cases to ensure all functionalities are operational.

::

    py.test -v

If ``pytest`` is not installed, you may want to run the following command:

::

    pip install -r tests/requirements.txt


Deployment
==========

Deploy a source package (to `pypi <https://pypi.org>`_) as follows:

::

    python setup.py sdist upload

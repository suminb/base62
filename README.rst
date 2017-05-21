|Build Status|

A Python module for base62 encoding. Ported from PHP code that I wrote
in mid-2000, which can be found on
`here <http://blog.suminb.com/archives/558>`__.

Installation
------------

|PyPI|

::

    pip install pybase62

Usage
-----

.. code:: python

    >>> import base62

    >>> base62.encode(34441886726)
    'base62'

    >>> base62.decode('base62')
    34441886726

.. |Build Status| image:: https://travis-ci.org/suminb/base62.svg?branch=master
   :target: https://travis-ci.org/suminb/base62
.. |PyPI| image:: https://img.shields.io/pypi/v/pybase62.svg
   :target: https://pypi.python.org/pypi/pybase62


Tests
-----

You may run some test cases to ensure all functionalities are operational.

::

    py.test -v

If ``pytest`` is not installed, you may want to run the following commands:

::

    pip install -r tests/requirements.txt

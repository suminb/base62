A Python module for base62 encoding. Ported from PHP code that I wrote in mid-2000, which can be found on [here](http://blog.suminb.com/archives/558).

Installation
------------

    sudo pip install pybase62


Usage
------

    >>> import base62

    >>> base62.encode(34441886726)
	'base62'

	>>> base62.decode('base62')
    34441886726

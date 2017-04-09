
"""
Original PHP code from http://blog.suminb.com/archives/558
"""

__author__ = 'Sumin Byeon'
__email__ = 'suminb@gmail.com'
__version__ = '0.1.3'

CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BASE = 62


def bytes_to_int(s):
    """Converts a byte array to an integer value. Python 3 comes with a
    built-in function to do this, but we would like to keep our code Python 2
    compatible.

    NOTE: Big-endian is assumed.
    """
    n = len(s)
    cs = list(bytearray(s))
    ds = [x << (8 * (n - 1 - i)) for i, x in enumerate(cs)]

    return sum(ds)


def encode(n):
    """Encodes a given integer ``n``."""

    s = []
    while n > 0:
        r = n % BASE
        n //= BASE

        s.append(CHARSET[r])

    if len(s) > 0:
        s.reverse()
    else:
        s.append('0')

    return ''.join(s)

def decode(b):
    """Encodes a base62 encoded value ``b``."""

    if b.startswith('0z'):
        b = b[2:]

    l, i, v = len(b), 0, 0
    for x in b:
        v += __value__(x) * (BASE**(l-(i+1)))
        i += 1

    return v

def __value__(ch):
    """Decodes an individual digit of a base62 encoded string."""

    if ch in '01234567890':
        return ord(ch) - ord('0')
    elif ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return ord(ch) - ord('A') + 10
    elif ch in 'abcdefghijklmnopqrstuvwxyz':
        return ord(ch) - ord('a') + 36
    else:
        raise RuntimeError('base62: Invalid character (%s)' % ch)

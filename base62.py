
#
# Original PHP code from http://blog.suminb.com/archives/558
#

CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
BASE = 62

def encode(n):
    s = []
    while n > 0:
        r = n % BASE
        n /= BASE

        s.append(CHARSET[r])

    s.reverse()

    return ''.join(s)

def decode(b):
    if b.startswith('0z'):
        b = b[2:]

    l, i, v = len(b), 0, 0
    for x in b:
        v += __value__(x) * (BASE**(l-(i+1)))
        i += 1

    return v

def __value__(ch):
    if ch in '01234567890':
        return ord(ch) - ord('0')
    elif ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return ord(ch) - ord('A') + 10
    elif ch in 'abcdefghijklmnopqrstuvwxyz':
        return ord(ch) - ord('a') + 36
    else:
        raise RuntimeError('base62: Invalid character (%s)' % ch)

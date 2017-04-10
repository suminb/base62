import pytest

import base62


bytes_int_pairs = [
    (b'\x00', 0),
    (b'\x01', 1),
    (b'\x01\x01', 0x0101),
    (b'\xff\xff', 0xffff),
    (b'\x01\x01\x01', 0x010101),
    (b'\x01\x02\x03\x04\x05\x06\x07\x08', 0x0102030405060708),
]


def test_basic():
    assert base62.encode(0) == '0'
    assert base62.decode('0') == 0

    assert base62.encode(34441886726) == 'base62'
    assert base62.decode('base62') == 34441886726


@pytest.mark.parametrize('b, i', bytes_int_pairs)
def test_bytes_to_int(b, i):
    assert base62.bytes_to_int(b) == i


@pytest.mark.parametrize('b, i', bytes_int_pairs)
def test_encodebytes(b, i):
    assert base62.encodebytes(b) == base62.encode(i)


@pytest.mark.parametrize('s', ['0', '1', 'a', 'z', 'ykzvd7ga'])
def test_decodebytes(s):
    assert base62.bytes_to_int(base62.decodebytes(
        s.encode(base62.DEFAULT_ENCODING))) == base62.decode(s)

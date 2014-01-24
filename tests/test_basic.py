import base62

def test_basic():
    assert base62.encode(34441886726) == 'base62'
    assert base62.decode('base62') == 34441886726

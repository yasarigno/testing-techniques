from hello import addThis

def test_addThis():
    assert addThis(4, 8) == 12
    assert addThis("1",2) == 3
    assert addThis(3,5) == 8        # gives a false error if you set it != 8

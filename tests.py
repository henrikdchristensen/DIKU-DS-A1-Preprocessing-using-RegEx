from testbook import testbook
@testbook('book.ipynb', execute=True)

def test_find_century(tb):
    func = tb.ref("find_century")
    
    # Within range cases:
    assert func(4122, 38) == 1900
    
    # Edge cases:
    
    # Boundary cases:
    
    # Outside range cases:
    
    
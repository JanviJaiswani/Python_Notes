import pytest

@pytest.mark.parametrize("a , b , result",[(1,2,3),(1,2,3),(3,6,9)])
def testaddItemCart(a,b,result):
    assert a + b == result
    

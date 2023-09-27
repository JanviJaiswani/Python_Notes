def test_pass():
    assert 1+1 == 2
    
def test_fail():
    assert 2+3 == 5

def add(x,y):
    return x+y

def test_add():
    result = add(5,6)
    assert result == 10
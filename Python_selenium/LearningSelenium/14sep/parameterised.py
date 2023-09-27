import pytest

@pytest.fixture(params=["a","b"])
def setup(request):
    print(request.param)
    
def testaddItemCart(setup):
    print("Item Added!")
    
def testItemremoved():
    print("Item Removed!!")
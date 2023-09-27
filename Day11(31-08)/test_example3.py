from example import *
import pytest 

@pytest.fixture
def bob():
    return {"name":"bob"}

def test_hi(bob):
    assert hi(bob) == "hi bob"
    
def test_hello(bob):
    assert hello(bob) == "hello bob"
    
def test_how_are_u(bob):
    assert how_are_u(bob) == "how are u bob"
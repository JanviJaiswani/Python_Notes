import pytest

def testLogIn():
    print("you have logged in!!")

@pytest.mark.testing
def testLogOff():
    print("LogOut!!")


def testcalc():
    assert 2 + 2 == 6
import pytest

@pytest.fixture
def setup(scope="session",autouse=True):
    print("Launch")
    print("Browser Product!")
    yield
    print("Log off!")
    print("Finished!")
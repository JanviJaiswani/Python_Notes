import pytest

@pytest.mark.usefixtures(setup)
class Test():
    def test_search():
        
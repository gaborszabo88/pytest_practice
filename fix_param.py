import pytest


@pytest.fixture
def res():
    return 200


@pytest.mark.parametrize("x,y",[(10,20), (20,30)])
def test_method(res, x, y):
    assert x*y == res


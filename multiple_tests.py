import pytest


@pytest.mark.webtest
def test_method1():
    assert 1 == 2


@pytest.mark.apitest
def test_method2():
    assert 2 == 2


import pytest


@pytest.fixture
def before_after():
    print('Begin')
    yield
    print('\nAfter')


def test_demo1(before_after):
    assert 1 == 1


def test_demo2():
    assert 2 != 1

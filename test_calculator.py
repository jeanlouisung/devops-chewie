import pytest

from calculator import add


def test_throw_error_if_not_number():
    with pytest.raises(TypeError):
        add('1', '2')


def test_return_0():
    res = add(0, 0)
    assert res == 0

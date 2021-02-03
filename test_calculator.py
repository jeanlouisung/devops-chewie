import pytest

from calculator import add


def test_throw_error_if_not_number():
    with pytest.raises(TypeError):
        add('1', '2')

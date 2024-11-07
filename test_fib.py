import pytest

from fib import fibonacci


def test_fib_9_is_34():
    assert fibonacci(9) == 34

def test_fib_9_is_34_2():
    with pytest.raises(ValueError):
        fibonacci(-1)
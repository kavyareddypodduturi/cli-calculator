from calculator.operations import add, subtract, multiply, divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(5, 0) == "Cannot divide by zero"

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (-1, 1, 0),
    ],
)
def test_add_param(a, b, expected):
    assert add(a, b) == expected

import pytest
from src.main import add, subtract, multiply, divide

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b



@pytest.fixture
def numbers():
    return 10, 5
# 🔹 TEST + FIXTURE
def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == 5


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 0, 0),
    (-2, 4, -8)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_subtract(numbers):
    a, b = numbers
    assert subtract(a, b) == 5
def test_divide():
    assert divide(10, 2) == 5



def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

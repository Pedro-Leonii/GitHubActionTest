import pytest
from functions import fibonacci

def test_fib_on_0():
    assert fibonacci(0) == 1

def test_fib_on_1():
    assert fibonacci(1) == 1

def test_fib_on_10():
    assert fibonacci(10) == 55

def test_fib_on_negative():
    assert fibonacci(-1) == 0

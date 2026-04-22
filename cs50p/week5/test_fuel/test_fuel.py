'''
from fuel import convert, gauge imports both functions so we can test them directly.
import pytest is needed to use pytest.raises() for testing exceptions.

Each function must start with test_ so pytest can automatically find and run it.
assert checks that the expression is True — if not, the test fails.

test_fuel: checks that a normal fraction converts correctly and gauge returns percentage.
test_empty_fuel: checks that 0/4 converts to 0 and gauge returns "E".
test_full_fuel: checks that 4/4 converts to 100 and gauge returns "F".

test_zero_division: checks that convert() raises ZeroDivisionError when Y is 0.
test_value_error: checks that convert() raises ValueError when X is greater than Y.
test_negative_values: checks that convert() raises ValueError for negative values.

pytest.raises() is a context manager — the code inside the with block is expected
to raise the specified exception. If it does not, the test fails.
'''

import pytest
from fuel import convert, gauge

def test_fuel():
    assert convert("1/2") == 50
    assert gauge(50) == "50%"

def test_empty_fuel():
    assert convert("0/4") == 0
    assert gauge(0) == "E"

def test_full_fuel():
    assert convert("4/4") == 100
    assert gauge(100) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("5/4")

def test_negative_values():
    with pytest.raises(ValueError):
        convert("-1/-2")
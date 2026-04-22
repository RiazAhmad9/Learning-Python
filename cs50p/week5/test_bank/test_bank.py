'''
from bank import value imports only the value function from bank.py
so we can call it directly without bank.value().

Each function must start with test_ so pytest can automatically find and run it.

assert checks that the expression is True. If it is, the test passes.
If it is not, the test fails and pytest tells you which assertion broke.

test_hello: checks that a greeting starting with "hello" returns 0.
test_with_h: checks that a greeting starting with "h" but not "hello" returns 20.
test_no_h: checks that a greeting not starting with "h" returns 100.
test_uppercase: checks that value() handles uppercase input correctly,
since normalization happens inside value() not before it is called.
'''

from bank import value

def test_hello():
    assert value("hello") == 0

def test_with_h():
    assert value("hi") == 20

def test_no_h():
    assert value("nice to meet you") == 100

def test_uppercase():
    assert value("Hello") == 0


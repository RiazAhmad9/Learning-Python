'''
from plates import is_valid imports only the is_valid function from plates.py
so we can call it directly without plates.is_valid().

Each function must start with test_ so pytest can automatically find and run it.

assert checks that the expression is True. If it is, the test passes.
If it is not, the test fails and pytest tells you which assertion broke.

test_2_to_6_cha: checks that plates longer than 6 characters are rejected.
test_two_letters: checks that plates not starting with two letters are rejected.
test_num_0: checks that plates with a number sequence starting with 0 are rejected.
test_letter: checks that letters appearing after numbers are rejected.
test_punctuation: checks that non-alphanumeric characters are rejected.
test_correct: checks that a valid plate passes all rules and returns True.
'''

from plates import is_valid

def test_2_to_6_cha():
    assert is_valid("ar96530") == False

def test_two_letters():
    assert is_valid("k90658") == False

def test_num_0():
    assert is_valid("kr0986") == False

def test_letter():
    assert is_valid("kr89kt") == False

def test_punctuation():
    assert is_valid("kr98.6") == False

def test_correct():
    assert is_valid("CS50") == True

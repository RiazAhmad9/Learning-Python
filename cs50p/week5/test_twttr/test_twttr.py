'''
from twttr import shorten imports only the shorten function from twttr.py
so we can call it directly without twttr.shorten().

Each function must start with test_ so pytest can automatically find and run it.

assert checks that the expression is True. If it is, the test passes.
If it is not, the test fails and pytest tells you which assertion broke.

test_lowercase_vowels: checks that lowercase vowels are removed.
test_uppercase_vowels: checks that uppercase vowels are also removed.
test_no_vowels: checks that non-vowel characters pass through untouched.
test_all_vowels: checks that a string of only vowels returns an empty string.
'''

from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"

def test_no_vowels():
    assert shorten("try") == "try"

def test_all_vowels():
    assert shorten("EAU") == ""
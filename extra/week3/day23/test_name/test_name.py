"""
Limitations: Scottish/Irish surname can not pass.

"""
from name_cleaner import name_clean

def test_name_spaces():
    name = name_clean("  john   doe  ")
    assert name == "John Doe"

def test_name_uppercase():
    name = name_clean("JOHN DOE")
    assert name == "John Doe"

def test_name_lowercase():
    name = name_clean("john doe")
    assert name == "John Doe"

def test_name_mixed():
    name = name_clean("  jOhN   dOe  ")
    assert name == "John Doe"

def test_name_number():
    name = name_clean("john123doe")
    assert name == "John Doe"

def test_name_Apostrophe():
    name = name_clean("O'brien")
    assert name == "O'Brien"

def test_name_scottish_irish():
    name = name_clean("mcdonald")
    assert name == "McDonald"
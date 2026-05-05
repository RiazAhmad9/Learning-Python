"""
Limitations: 1.TLD will accept any letter between 2 and 6.
"""
from email_validator import validate_email

def test_normal_email():
    email = validate_email("test@example.com")
    assert email == True

def test_dot_email():
    email = validate_email("test.test@example.com")
    assert email == True

def test_plus_email():
    email = validate_email("test+test@example.com")
    assert email == True

def test_underscore_email():
    email = validate_email("test_test@example.com")
    assert email == True

def test_long_tld_email():
    email = validate_email("test@example.museum")
    assert email == True

def test_missing_email():
    email = validate_email("testexample.com")
    assert email == False

def test_missing_tld_email():
    email = validate_email("test@example")
    assert email == False

def test_spaces_email():
    email = validate_email("test    @example.com")
    assert email == False

def test_double_email():
    email = validate_email("test@@example.com")
    assert email == False

def test_empty_email():
    email = validate_email("")
    assert email == False
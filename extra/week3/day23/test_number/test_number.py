from number_validator import validate_number

def test_something():
    result = validate_number("some text with 123")
    assert result == ["123"]

def test_number_code():
    result = validate_number("+61 412 345 678")
    assert result == ["+61 412 345 678"]

def test_number_normal():
    result = validate_number("0412 345 678")
    assert result == ["0412 345 678"]

def test_number_parenthesis():
    result = validate_number("(02) 1234 5678")
    assert result == ["(02) 1234 5678"]

def test_text():
    result = validate_number("some text with")
    assert result == []

def test_empty():
    result = validate_number("")
    assert result == []

def test_multiple_number():
    result = validate_number("call me at 123 or 456")
    assert result == ["123", "456"]
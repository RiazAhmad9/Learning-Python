from seasons import minutes_to_word, conv
import pytest


def test_minutes_to_word_year():
    assert minutes_to_word(525600) == "five hundred twenty-five thousand, six hundred minutes"
    assert minutes_to_word(1051200) == "one million, fifty-one thousand, two hundred minutes"


def test_conv():
    with pytest.raises(SystemExit):
        conv("")
    
    with pytest.raises(SystemExit):
        conv("2099-01-01")

    with pytest.raises(SystemExit):
        conv("01-01-1990")

    with pytest.raises(SystemExit):
        conv("05-09-2026")
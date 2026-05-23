from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(12.5)
    with pytest.raises(ValueError):
        Jar("twelve")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):   
        jar.deposit(-1)
    with pytest.raises(ValueError):   
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):   
        jar.withdraw(-1)
    with pytest.raises(ValueError):   
        jar.withdraw(13)
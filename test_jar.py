import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)  # Invalid capacity

    with pytest.raises(ValueError):
        Jar("ten")  # Invalid capacity type

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(8)  # Exceeds capacity

def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(3)
    assert jar.size == 4

    with pytest.raises(ValueError):
        jar.withdraw(5)

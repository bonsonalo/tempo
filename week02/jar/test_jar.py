import pytest
from jar import Jar



""" Test for _init_ method """
def test_init_valid():
    j = Jar(5)
    assert j.capacity == 5
    assert j.size == 0

def test_init_invalid():
    with pytest.raises(ValueError):
        j = Jar(-1) # it can't be negative
    with pytest.raises(ValueError):
        j = Jar("Hey") # it can't be string
    
""" Test for _str__ method """

def test_str_empty():
    j = Jar(5)
    assert str(j) == ""

def test_str_with_cookies():
    j = Jar(5)
    j.deposit(2)
    assert str(j) == "🍪🍪"


""" Test for depost method """
def test_deposit_valid():
    j = Jar(5)
    j.deposit(3)
    assert j.size == 3

def test_deposit_too_much():
    j = Jar(5)
    j.deposit(4)
    with pytest.raises(ValueError):
        j.deposit(2)

""" test for withdraw method """

def test_withdraw_valid():
    j = Jar(5)
    j.deposit(5)
    j.withdraw(4)
    assert j.size == 1

def test_withdraw_invalid():
    j = Jar(5)
    j.deposit(4)
    j.withdraw(3)
    with pytest.raises(ValueError):
        j.withdraw(2)     # not that much cookies available

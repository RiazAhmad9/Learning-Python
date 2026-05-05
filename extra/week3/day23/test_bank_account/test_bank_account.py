"""
Limitations: 1.Negetive numbers are accepted
             2.BankAccount accepts a string
"""
from bank_account import BankAccount

def test_account():
    account = BankAccount(1000)
    assert account.account == 1000

def test_account_zero_balance():
    account = BankAccount(0)
    assert account.account == 0

def test_account_negative_balance():
    account = BankAccount(-500)
    assert account.account == -500

def test_account_str_value():
    account = BankAccount("hello")
    assert account.account == "hello"

def test_str():
    account = BankAccount(1000)
    assert str(account) == "1000"

def test_str_zero_value():
    account = BankAccount(0)
    assert str(account) == "0"

def test_bonus():
    account_bonus = BankAccount.with_bonus(1000, 200)
    assert account_bonus.account == 1200

def test_bonus_float():
    account_bonus = BankAccount.with_bonus(1000.0, 200.0)
    assert account_bonus.account == 1200.0


def test_bonus_zero_amount():
    account_bonus = BankAccount.with_bonus(1000, 0)
    assert account_bonus.account == 1000

def test_bonus_negative_amount():
    account_bonus = BankAccount.with_bonus(1000, -200)
    assert account_bonus.account == 800
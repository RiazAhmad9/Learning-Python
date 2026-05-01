"""
BankAccount Class — OOP Fundamentals(classmethod)
===================================
Demonstrates a basic class with attributes and methods.

Class:
    BankAccount(account)
        Attributes:
            account (float) — starting balance of the account

        Methods:
            __str__()                 → returns account
            with_bonus(amount, bonus) → returns new BankAccount with amount + bonus

main():
    Creates an account with starting amount of 1000.
    Creates an account with starting amount of 1000 and 200 bonus.
    prints both account.
"""
class BankAccount:
    def __init__(self, account):
        self.account = account

    def __str__(self):
        return f"{self.account}"
    
    @classmethod
    def with_bonus(cls, amount, bonus):
        return cls(amount + bonus)

def main():
    account = BankAccount(1000)
    account_bonus = BankAccount.with_bonus(1000, 200)
    print(f"Account: {account}\nAccount with bonus: {account_bonus}")

if __name__ == "__main__":
    main()
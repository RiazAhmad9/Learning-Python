"""
Bank Class — OOP Fundamentals
===================================
Demonstrates a basic class with attributes and methods.

Class:
    Bank(balance)

    Attributes:
        balance (float) — starting balance of the account

    Methods:
        deposit(amount)  → adds amount to balance
        withdraw(amount) → subtracts amount from balance;
                           raises ValueError if amount exceeds balance
        get_balance()    → returns current balance

main():
    Creates an account with starting balance of 1000.
    Prompts user to deposit, withdraw, or check balance.
    Rejects non-positive amounts. Loops until EOFError.
"""
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


def main():
    account = Bank(1000)
    while True:
        try:
            option = input("1.Deposit\n2.Withdraw\n3.Balance\nOption: ").lower()
            if option == "1" or option == "deposit":
                while True:
                    try:
                        amount = float(input("Amount: "))
                        if amount <= 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Enter a valid amount")
                account.deposit(amount)
                print(f"{amount} has been deposited\nCurrent balance: {account.balance}")
            
            elif option == "2" or option == "withdraw":
                while True:
                    try:
                        amount = float(input("Amount: "))
                        if amount <= 0:
                            raise ValueError("Enter a valid amount")
                        break
                    except ValueError as message:
                        print(message)
                try:
                    account.withdraw(amount)
                    print(f"{amount} has been withdrawn\nCurrent balance: {account.balance}")
                except ValueError as message:
                    print(message)

            elif option == "3" or option == "balance":
                print(f"Current balance: {account.get_balance()}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
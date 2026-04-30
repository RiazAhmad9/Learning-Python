"""
Counter Class — OOP Fundamentals
===================================
Demonstrates a basic class with attributes and methods.

Class:
    Counter(value)

    Attributes:
        value (int) — starting value of the counter

    Methods:
        increment()  →  adds '1' to value
        decrement()  →  subtracts amount from value;
                        raises ValueError if subtraction exceeds value
        reset()      →  resets current value

main():
    Creates an balance with starting balance of 0.
    Prompts user to increment, decrement, or reset balance.
    Rejects non-positive amounts. Loops until EOFError.
"""
class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value <= 0:
            raise ValueError("Insufficient value")
        self.value -= 1

    def reset(self):
        self.value = 0


def main():
    balance = Counter(0)
    while True:
        try:
            option = input("1.Increment\n2.Decrement\n3.Reset\nOption: ").lower()
            if option == "1" or option == "increment":
                balance.increment()
                print(f"Added\nCurrent value: {balance.value}")
            
            elif option == "2" or option == "decrement":
                try:
                    balance.decrement()
                    print(f"Subtracted\nCurrent value: {balance.value}")
                except ValueError as message:
                    print(message)

            elif option == "3" or option == "reset":
                balance.reset()
                print(f"Reset\nCurrent value: {balance.value}")
        except EOFError:
            break


if __name__ == "__main__":
    main()
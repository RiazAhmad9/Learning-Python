"""
Counter Class — OOP Fundamentals __str__
===================================
Demonstrates a basic class with attributes and methods.

Class:
    Counter(count)

    Attributes:
        count (int) — starting value of the counter

    Methods:
        increment()  →  adds '1' to count
        decrement()  →  subtracts amount from count;
                        raises ValueError if subtraction exceeds count
        reset()      →  resets current count
        __str__()    →  returns "Count: {count}"

main():
    Creates a counter starting at 0.
    Prompts user to increment, decrement, or reset.
    Loops until EOFError.
"""
class Counter:
    def __init__(self, count):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count <= 0:
            raise ValueError("Insufficient value")
        self.count -= 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"Count: {self.count}"


def main():
    value = Counter(0)
    while True:
        try:
            option = input("1.Increment\n2.Decrement\n3.Reset\nOption: ").lower()
            if option == "1" or option == "increment":
                value.increment()
                print(value)
            
            elif option == "2" or option == "decrement":
                try:
                    value.decrement()
                    print(value)
                except ValueError as message:
                    print(message)

            elif option == "3" or option == "reset":
                value.reset()
                print(value)
        except EOFError:
            break

if __name__ == "__main__":
    main()
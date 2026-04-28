"""
simple_calculator
--------------------
Takes two numbers and an operator, prints the result.

- operators list: single source of truth for valid operators, used for validation
- second == 0 + continue: blocks division by zero before it reaches calc()
- while True (operator loop): loops until a valid operator is entered
- calc(first, second, operator): separates computation from input logic
- if/elif chain in calc(): maps operator string to the correct arithmetic
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

operators = ["+", "-", "*", "/"]
def main():
    while True:
        try:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            if second == 0:
                print("Second number cannot be zero")
                continue
            break
        except ValueError:
            print("Numbers only")

    while True:
        operator = input("Operator: ")
        if operator not in operators:
            print("Chose between (+, -, *, /)")
            continue
        break
    calc(first, second, operator)

def calc(first, second, operator):
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
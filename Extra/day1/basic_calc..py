"""
basic_calculator
-------------------
Takes two float inputs and prints sum, difference, product, division, remainder.

- float(): accepts decimal numbers, raises ValueError on non-numeric input
- while True + try/except: loops until valid input, catches invalid entries
- second == 0 + continue: blocks division by zero, re-asks without crashing
- :.2f: formats division to 2 decimal places
"""

while True:
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        if second == 0:
            print("Second number cannot be zero")
            continue
        break
    except ValueError:
        print("Input only numbers")

print(f"Sum = {first + second}\nDiff = {first - second}\nProd = {first * second}\ndiv = {(first / second):.2f}\nRem = {first % second}")
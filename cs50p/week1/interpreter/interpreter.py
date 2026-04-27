"""
interpreter.py
------------------------
Takes a arithmetic expression as a single input and calculates the result.

Example input: 3 + 5 or 10 / 2

- .split(): splits input into three parts — x, operator, z
- unpacking x, y, z: expects exactly three items, raises ValueError otherwise
- float(): converts operands, raises ValueError on non-numeric input
- exit(): terminates cleanly after any error instead of crashing on undefined result
- z != 0: blocks division by zero before it happens
- :.1f: formats result to 1 decimal place
"""

expression = input("Expression: ")

try:
    x, y, z = expression.split()
    x, z = float(x), float(z)
except ValueError:
    print("Invalid format")
    exit()

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    if z != 0:
        result = x / z
    else:
        print("Cannot divide by zero")
        exit()
else:
    print("Invalid format")
    exit()

print(f"{result:.1f}")
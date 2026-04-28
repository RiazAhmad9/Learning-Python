"""
largest_of_three
-------------------
Takes three numbers and prints the largest.

- float(): accepts decimals, raises ValueError on non-numeric input
- while True + try/except: loops until all three inputs are valid
- max(): built-in that returns the largest value among given arguments
"""

while True:
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        c = float(input("Third number: "))
        break
    except ValueError:
        print("Enter only numbers")

print("The largest number is:", max(a, b, c))
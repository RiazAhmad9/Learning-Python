"""
even_odd_checker
-------------------
Checks whether a given integer is even or odd.

- int(): whole numbers only, floats make no sense for even/odd checks
- while True + try/except: loops until valid input, catches non-numeric entries
- number % 2 == 0: modulo returns remainder — 0 means evenly divisible by 2
- ternary operator: concise single-line if/else for simple conditions
"""

while True:
    try:
        number = int(input("Number: "))
        break
    except ValueError:
        print("Enter a whole number")

print("Even" if number % 2 == 0 else "Odd")
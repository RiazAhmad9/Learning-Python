"""
number_sign_checker
----------------------
Checks whether a number is positive, negative, or zero.

- float(): accepts decimals and negatives, raises ValueError on non-numeric input
- while True + try/except: loops until valid input
- if/elif/else: three mutually exclusive conditions cover all possible cases
"""

while True:
    try:
        number = float(input("Number: "))
        break
    except ValueError:
        print("Enter a number")

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is Zero")       
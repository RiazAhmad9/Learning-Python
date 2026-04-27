"""
number_range_input
---------------------
Prompts the user for a number between 1 and 10, rejecting invalid input.

- int(): whole numbers only, raises ValueError on non-numeric input
- 0 < number <= 10: chained comparison, checks range in one expression
- while True + try/except: loops until valid input is entered
"""

while True:
    try:
        number = int(input("Number(1-10): "))
        if 0 < number <= 10:
            break
        print("Must be between (1-10)")
    except ValueError:
        print("Enter a whole number")
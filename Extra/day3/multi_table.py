"""
multiplication_table
-----------------------
Prints the multiplication table (1-10) for a given number.

- int(): whole numbers only, decimals make no sense for a times table
- while True + try/except: loops until valid input, catches non-numeric entries
- range(1, 11): generates multipliers from 1 to 10 inclusive
"""

while True:
    try:
        number = int(input("Number: "))
        break
    except ValueError:
        print("Enter a whole number")

for integer in range(1, 11):
    print(f"{number} x {integer} = {number * integer}")
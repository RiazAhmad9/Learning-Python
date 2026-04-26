"""
age_conversion
-----------------
Takes a birth year and calculates the user's current age.

- datetime.date.today().year: dynamically fetches current year, no hardcoding
- int(): birth years are whole numbers, floats make no sense here
- while True + try/except: loops until valid input, catches non-numeric entries
- range check (1900 to current year - 1): blocks impossible or future birth years
"""

from datetime import date

while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        if 1900 <= birth_year <= (date.today().year - 1):
            break
        print(f"Enter a year between (1900-{date.today().year})")
    except ValueError:
        print("Enter numbers only")

print(f"You are {date.today().year - birth_year} years old")
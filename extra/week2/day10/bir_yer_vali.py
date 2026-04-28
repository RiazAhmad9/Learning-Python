"""
birth_year_validator
-----------------------
Prompts the user for a valid birth year between 1900 and the current year.

- from datetime import date: imports only what's needed, allows date.today().year
- int(): whole numbers only, raises ValueError on non-numeric input
- 1900 <= year <= date.today().year: chained comparison, dynamically uses current year
- while True + try/except: loops until valid input is entered
"""

from datetime import date

while True:
    try:
        year = int(input("Birth year: "))
        if 1900 <= year <= date.today().year:
            break
        print(f"Enter a valid birth year (1900-{date.today().year})")
    except ValueError:
        print("Input whole numbers")
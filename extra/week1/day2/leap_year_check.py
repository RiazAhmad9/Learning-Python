"""
leap_year_checker
--------------------
Checks whether a given year is a leap year.

- int(): years are whole numbers, floats make no sense here
- while True + try/except: loops until valid input, catches non-numeric entries
- leap year logic: divisible by 4 AND not by 100, OR divisible by 400
  (e.g. 1900 is not a leap year, but 2000 is)
"""

while True:
    try:
        number = int(input("Year: "))
        break
    except ValueError:
        print("Enter only numbers")

if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0):
    print(f"{number} is leap year")
else:
    print(f"{number} is not leap year")
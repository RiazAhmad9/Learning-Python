"""
Password validator using regex.

Pattern breakdown:
- Password: 1.Checks for 8 or more characters with atleast a number and an uppercase letter.
            2.With the help of boolean flag loops through untill valid password.
            3.For each check prints a specific error message.

- Limitations: Spaces are not disallowed.
"""
import re


while True:
    password = input("Password: ")
    valid = True

    if not re.search(r".{8,}", password):
        print("Need atleast 8 characters")
        valid = False
    if not re.search(r"[A-Z]+", password):
        print("Need atleast 1 uppercase letter")
        valid = False
    if not re.search(r"\d+", password):
        print("Need atleast 1 number")
        valid = False
    if valid:
        print("Valid")
        break
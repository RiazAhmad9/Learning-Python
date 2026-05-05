"""
Email validator using regex.

Pattern breakdown:
- local part: allows multiple character from alphabet a to z in both lower 
    and upper case and as well as (+, _) sign and allows to take a optional 
    dot along with those specific characters.

- @: exactly one is necessary between local and domain part.

- domain: same aslike local part.

- TLD: takes only lower case alphabets upto 2 to 6.
"""
import re


def validate_email(email):
    if re.fullmatch(r"[a-zA-Z0-9_+]+(\.[a-zA-Z0-9_+]+)*@[a-zA-Z0-9_+]+(\.[a-zA-Z0-9_+]+)*\.([a-z]{2,6})", email):
        return True
    else:
        return False

def main():
    email = input("Email: ")
    if validate_email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
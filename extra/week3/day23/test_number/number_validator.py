"""
Number validator using regex.

Pattern breakdown:
- Country code: Allows either starting from '+' sign and 1 to 3 numbers and at 
                the end any of these ('-', '.', ' ') sign or 1 to 3 numbers 
                surrounded with parenthesis following with a whitespace.

- Local number: Allows one or more numbers with optional pattern of ('-', '.', ' ') sign and numbers.

- Limitations: No limit in digit count for local number.
"""
import re


def validate_number(text):
    number = re.findall(r"(?:\+\d{1,3}[\s\-\.]|\(\d{2,3}\)?[\s])?\d+(?:[\s\-\.]?\d+)*", text)
    return number

def main():
    text = input("Text: ")
    print(f"Number: {validate_number(text)}")

if __name__ == "__main__":
    main()
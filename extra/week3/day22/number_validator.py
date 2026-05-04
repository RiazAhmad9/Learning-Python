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


text = input("Text: ")
number = re.findall(r"(?:\+\d{1,3}[\s\-\.]|\(\d{2,3}\)?[\s])?\d+(?:[\s\-\.]?\d+)*", text)
print(f"Number: {number}")
"""
palindrome_checker
---------------------
Checks whether a given word reads the same forwards and backwards.

- .lower(): normalises input so 'Racecar' and 'racecar' are treated the same
- [::-1]: slices the string in reverse order
- compares reversed string to original to determine if it's a palindrome
"""

text = input("Word: ")
lower_text = text.lower()
if lower_text[::-1] == lower_text:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
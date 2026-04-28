"""
camel.py
-----------------
Converts camelCase input to snake_case.

- isupper(): detects uppercase letters
- "_" + i.lower(): prepends underscore and lowercases the letter
- final +=: builds the result string character by character
"""

text = input("camelCase: ")
final = ""

for letter in text:
    if letter.isupper():
        final += "_" + letter.lower()
    else:
        final += letter

print("snake_case:", final)
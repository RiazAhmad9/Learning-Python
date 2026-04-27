"""
file_reader
--------------
Opens and reads a file by name without crashing if it doesn't exist.

- .strip(): removes accidental whitespace from filename input
- open(name, "r"): opens file in read mode
- with statement: automatically closes the file after reading, even if an error occurs
- FileNotFoundError: caught if the file doesn't exist, prints a clean message instead of crashing
"""

name = input("Filename: ").strip()
try:
    with open(name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"{name} not found")
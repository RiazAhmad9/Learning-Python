"""
file_sorter
--------------
Reads a text file and prints its lines sorted alphabetically and numbered.

- open("name.txt", "r"): opens in read mode, raises FileNotFoundError if missing
- sorted(file): iterates over lines and sorts them alphabetically
- enumerate(..., 1): pairs each line with a number starting at 1
- .rstrip(): removes trailing newline characters from each line for clean output
- FileNotFoundError: caught if file doesn't exist, prints a clean message
"""

try:
    with open("name.txt", "r") as file:
        for number, name in enumerate(sorted(file), 1):
            print(f"{number}.{name.rstrip()}")
except FileNotFoundError:
    print("File not found")
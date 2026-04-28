"""
lines.py

Counts the number of lines of code in a given Python file,
excluding blank lines and comment lines (lines starting with '#').

Usage: python lines.py <filename.py>
Exits with an error if arguments are invalid, file is not .py, or file does not exist.
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")


counter = 0
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            line = line.lstrip()
            if line.strip() == "":
                continue
            elif line.startswith("#"):
                continue
            else:
                counter += 1
except FileNotFoundError:
    sys.exit("File not found")

print(counter)
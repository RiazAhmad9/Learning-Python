"""
sort_names
-------------
Reads names from a file, sorts them alphabetically, and writes to a new file.

- readlines(): reads all lines into a list, preserving each line as an element
- sorted(): returns a new alphabetically sorted list without modifying the original
- open(..., "w"): overwrites sorted_names.txt on every run
- .strip(): removes trailing newlines before rewriting each name cleanly
- combined with statement: opens both files in one line, closes both automatically
- FileNotFoundError: caught if names.txt doesn't exist
"""

try:
    with open("names.txt", "r") as infile, open("sorted_names.txt", "w") as outfile:
        names = infile.readlines()
        names = sorted(names)
        for name in names:
            outfile.write(f"{name.strip()}\n")
except FileNotFoundError:
    print("File not found")
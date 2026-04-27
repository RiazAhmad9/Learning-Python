"""
deep.py
------------
Prints 'Yes' if the user inputs 42, forty-two, or forty two.

- .strip().lower(): normalises input — removes whitespace and handles case
- valid = {...}: set of accepted answers — O(1) lookup, cleaner than chained if/elif
- ternary operator: concise single-line if/else for simple conditions
"""

text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
valid = {"42", "forty-two", "forty two"}
print("Yes" if text in valid else "No")
"""
twttr.py
----------------
Removes all vowels from the input string.

- alphabet.lower(): normalises each character to catch both uppercase and lowercase vowels
- {"a", "e", "i", "o", "u"}: set for O(1) lookup, faster than a list
- final +=: builds the result string character by character, skipping vowels
"""

text = input("Input: ")
final = ""

for alphabet in text:
    if alphabet.lower() not in {"a", "e", "i", "o", "u"}:
        final += alphabet

print(f"Output: {final}")
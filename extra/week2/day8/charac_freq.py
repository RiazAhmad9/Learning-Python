"""
character_frequency
----------------------
Counts how many times each letter appears in a given word or sentence.

- .lower().strip(): normalises input, removes leading/trailing whitespace
- string.punctuation: contains all punctuation characters
- .strip(string.punctuation): removes punctuation from each character
- .isalpha(): skips anything that isn't a letter (spaces, numbers, symbols)
- characters.get(clean, 0) + 1: returns current count or 0 if unseen, then increments
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
import string

def main():
    characters = {}
    word = input("Word: ").lower().strip()

    for letter in word:
        clean = letter.strip(string.punctuation)
        if not clean.isalpha():
            continue
        characters[clean] = characters.get(clean, 0) + 1

    for letter in characters:
        print(f"{letter} = {characters[letter]}")

if __name__ == "__main__":
    main()
"""
vowel_consonant_counter
--------------------------
Counts vowels and consonants in a given sentence.

- vowels = {...}: set for O(1) membership lookup, faster than a list
- .isalpha(): skips spaces, numbers, and punctuation
- .lower(): normalises each letter before checking against the vowels set
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    vowels = {"a", "e", "i", "o", "u"}
    vowel = 0
    consonant = 0
    text = input("Sentence: ")

    for letter in text:
        if letter.isalpha():
            if letter.lower() in vowels:
                vowel += 1
            else:
                consonant += 1

    print(f"Vowel = {vowel}\nConsonant = {consonant}")

if __name__ == "__main__":
    main()
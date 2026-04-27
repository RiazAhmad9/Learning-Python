"""
word_reverser
----------------
Reverses the order of words in a sentence.

- .split(): splits string into a list of words on whitespace
- [::-1]: slices the list in reverse order
- " ".join(): reassembles the reversed list back into a string
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    words = input("Input: ")
    print(f"Output: {convert(words)}")


def convert(words):
    return " ".join(words.split()[::-1])


if __name__ == "__main__":
    main()
"""
word_count
-------------
Counts lines, words, and characters in a given text file.

- open(file_name, "r"): opens file in read mode, raises FileNotFoundError if missing
- lines += 1: increments for every line iterated
- line.split(): splits line on whitespace into a list of words
- len(word): counts words in the list
- len(line): counts all characters in the line including spaces and newline
- FileNotFoundError: caught if file doesn't exist, prints a clean message
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    file_name = input("File: ")
    lines = 0
    words = 0
    characters = 0

    try:
        with open(file_name, "r") as file:
            for line in file:
                lines += 1
                word = line.split()
                words += len(word)
                characters += len(line)
            print(f"Lines: {lines}\nWords: {words}\nCharacters: {characters}")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
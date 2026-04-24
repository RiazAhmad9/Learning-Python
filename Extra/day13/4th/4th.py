'''
1.Three variables for each counter(characters,words,lines)
2.Splits the line for word count.
3.len to count items in a list for words and in a string for characters.
'''

file_name = input("File name: ")
lines = 0
words = 0
characters = 0

try:
    with open(f"{file_name}", "r") as file:
        for line in file:
            lines += 1
            word = line.split()
            words += len(word)
            characters += len(line)
        print(f"Lines: {lines}\nWords: {words}\nCharacters: {characters}")
except FileNotFoundError:
    print("File not found")
"""
capitalize_words
-------------------
Capitalises the first letter of every word in a sentence.

- .split(): splits sentence into a list of words on whitespace
- .capitalize(): uppercases first letter, lowercases the rest
- generator expression: applies .capitalize() to each word without
  building an intermediate list
- " ".join(): reassembles the words back into a single string
"""

text = input("Sentence: ")
print(" ".join(word.capitalize() for word in text.split()))
"""
sentence_reverser
--------------------
Reverses the order of words in a sentence.

- .split(): splits sentence into a list of words on whitespace
- [::-1]: slices the list in reverse order
- " ".join(): reassembles the reversed list back into a string
"""

text = input("Sentence: ")
print(f'Inverse: {" ".join(text.split()[::-1])}')
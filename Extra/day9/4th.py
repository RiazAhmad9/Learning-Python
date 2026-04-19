# Reversing words in a sentence

text = input("Sentence: ")
print(f"Inverse: {" ".join(text.split()[::-1])}")
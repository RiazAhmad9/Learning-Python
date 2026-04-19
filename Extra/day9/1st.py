# Capitalizing every word
text = input("Sentence: ")
print(" ".join(word.capitalize() for word in text.split()))
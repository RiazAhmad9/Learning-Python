# Printing 'Yes' if the user inputs 42 or forty-two or forty two.

# Asking for input and Converting the string to lower case as well as removing whitespace from both end.
text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# A set of answers from the condition.
valid = {"42", "forty-two", "forty two"}

# Printing the result by the condition.
print("Yes" if text in valid else "No")


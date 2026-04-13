# Removes vowels from the string.

# Takes input and stores initial output.
text = input("Input: ")
final = ""

# Loops until vowels are removed.
for i in text:
    if i in ["a", "e", "i", "o", "u"]:
        final += ""
    else:
        final += i

# Prints the final result.
print("Output:", final)

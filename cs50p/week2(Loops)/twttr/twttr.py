# Removes vowels from the string

# Stores input in 'text' variable
text = input("Input: ")
# Creates a 'final' variable to store value later on
final = ""

# Loops until vowels are removed
for i in text:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        final += ""
    else:
        final += i

# Prints the output
print("Output:", final)

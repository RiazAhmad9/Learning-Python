# Turns every uppercase into lowercase and adds '_' before it.

# User input and a initial output storage.
text = input("cameCase: ")
final = ""

# Adds character before uppercase words and convert it to lowercase.
for i in text:
    if i.isupper():
        final += "_" + i.lower()
    else:
        final += i

# Prints final result.
print("snake_case:", final)
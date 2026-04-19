# Turns every uppercase into lowercase and adds '_' before it

# Stores user input in 'text' variable 
text = input("cameCase: ")
# A varaible to store value later on
final = ""

# Adds character before uppercase words and converts it to lowercase
for i in text:
    if i.isupper():
        # Adds all character along with '_' if condition meets to 'final'
        final += "_" + i.lower()
    else:
        final += i

# Prints output
print("snake_case:", final)
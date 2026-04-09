#ask the user for their name
name =input("What's your name?")


#remove spaces from the name and capitalize the first letter of each word
name = name.strip().title()


#greet the user
print(f"Hello, {name}")

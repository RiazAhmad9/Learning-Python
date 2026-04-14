# A simple function to greet the input.

# Defined a function 'main' which takes input from user and prints the 'greet' functions message.
def main():
    x = input("What's your name? ")
    print(greet(x))

# Defines the function 'greet' which modifies the input.
def greet(name):
    return f"Greetings, {name}"

# Calls main.
main()

# A simple function to greet the user

# Function 'main' which stores input in 'x' variable and prints greeting message
def main():
    x = input("What's your name? ")
    print(greet(x))

# Function 'greet' which modifies the input
def greet(name):
    return f"Greetings, {name}"

# Calls 'main' function
main()

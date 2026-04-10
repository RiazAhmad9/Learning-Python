# Define a main function that prompts the user for their name and then calls the hello function with that name as an argument. The hello function should print a greeting to the user. If no name is provided, it should default to greeting "world".

# Defining the main function
def main():
    name = input("What is your name? ")
    hello(name)

# Defining the hello function that takes an optional argument 'to' with a default value of "world"
def hello(to="world"):
    print("hello,", to)
    
main()
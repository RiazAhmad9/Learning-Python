# A simple function to greet the user

def main():
    text = input("What's your name? ")
    print(greet(text))

def greet(name):
    return f"Greetings, {name}"
# if statement so file doesn't run on import
if __name__ == "__main__":
    main()
"""
greeter
----------
Takes the user's name and prints a greeting.

- greet(name): separate function handles greeting logic, main() handles input
- return: sends the string back to main() instead of printing inside greet(),
  keeping the function reusable and testable
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    name = input("What's your name? ")
    print(greet(name))


def greet(name):
    return f"Greetings, {name}"


if __name__ == "__main__":
    main()
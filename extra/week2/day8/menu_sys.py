"""
menu_system
--------------
Demonstrates a dictionary-based menu system.

- option dict: maps numeric keys to action labels — easy to extend by
  adding new key-value pairs without changing the loop logic
- text in option: checks if input matches a valid key
- EOFError: handles unexpected end of input (Ctrl+D / Ctrl+Z) gracefully
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    option = {
        "1": "Say Hello",
        "2": "Add two numbers",
        "3": "Quit",
    }
    while True:
        try:
            text = input("Option(1-3): ")
            if text in option:
                print(option[text])
            else:
                print("Invalid option")
            if text == "3":
                break
        except EOFError:
            break

if __name__ == "__main__":
    main()
"""
grocery.py
---------------
Collects grocery items until EOF (Ctrl+D / Ctrl+Z), then prints them
sorted alphabetically in uppercase with quantities.

- items = {}: dictionary to store item name as key, count as value
- .lower().strip(): normalises input — handles case and whitespace
- items.get(text, 0) + 1: increments count or starts at 1 if unseen
- EOFError: raised when user signals end of input, triggers sorted print
- sorted(items): returns alphabetically sorted list of keys
- item.upper(): prints item name in uppercase
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    items = {}
    while True:
        try:
            text = input().lower().strip()
            items[text] = items.get(text, 0) + 1
        except EOFError:
            for item in sorted(items):
                print(items[item], item.upper())
            break

if __name__ == "__main__":
    main()
"""
name_sorter
--------------
Collects names until EOF (Ctrl+D / Ctrl+Z), removes duplicates,
sorts alphabetically, and prints them numbered.

- .title().strip(): normalises input — capitalises first letter, removes whitespace
- .replace(" ", "").isalpha(): validates names allow spaces (e.g. "Ali Khan")
  but blocks numbers and special characters
- EOFError: raised when user signals end of input (Ctrl+D on Mac/Linux, Ctrl+Z on Windows)
- set(names): removes duplicate entries before sorting
- sorted(): returns alphabetically sorted list
- enumerate(..., 1): pairs each name with a number starting at 1
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    names = []
    while True:
        try:
            name = input("Name: ").title().strip()
            if name.replace(" ", "").isalpha():
                names.append(name)
            else:
                print("Names should only contain letters")
        except EOFError:
            break
    for number, name in enumerate(sorted(set(names)), 1):
        print(f"{number}.{name}")

if __name__ == "__main__":
    main()
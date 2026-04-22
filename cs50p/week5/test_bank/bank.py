'''
.strip() removes leading and trailing whitespace from the raw input.
We do NOT call .lower() on input() here — instead value() handles
case normalization internally with greeting.lower().startswith().
This way value() works correctly regardless of how it is called.

value() takes the greeting and returns the correct dollar amount as an int.
Order of conditions matters — "hello" must be checked before "h" because
every "hello" also starts with "h". Checking "h" first would swallow "hello".

if __name__ == "__main__" ensures main() only runs when the file is
executed directly, not when imported as a module by another file.
'''

def main():
    text = input("Greeting: ").strip()
    print(f"${value(text)}")

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
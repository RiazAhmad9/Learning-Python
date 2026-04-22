'''
.lower() converts the input to lowercase so "Hello" and "HELLO" are treated the same.
.strip() removes leading and trailing whitespace so " hello " still matches.
Both are chained directly on input() so we never store the raw version.

.startswith() checks if a string begins with the given substring.
Order matters here — "hello" is checked before "h" because every "hello"
also starts with "h". If we checked "h" first, "hello" would never be reached.
'''


text = input("Greeting: ").lower().strip()

if text.startswith("hello"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")
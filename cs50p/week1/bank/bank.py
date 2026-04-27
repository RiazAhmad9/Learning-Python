"""
bank.py
------------------
Charges different amounts based on how the user greets.

- .lower().strip(): normalises input — handles case and whitespace
- .startswith(): checks the beginning of the string
- order matters: "hello" checked before "h" — every "hello" starts with "h",
  so checking "h" first would prevent "hello" from ever being reached
"""

text = input("Greeting: ").lower().strip()

if text.startswith("hello"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")
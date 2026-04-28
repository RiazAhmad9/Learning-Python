"""
coke.py
-------------------
Simulates a coin exchange machine with a starting amount of 50 cents.

- pay = 50: starting amount due in cents
- {25, 10, 5}: valid coin denominations as a set for O(1) lookup
- pay -= payment: deducts valid coin from amount due
- abs(pay): handles overpayment — returns positive change owed
- continue: skips the if/else block if input was non-numeric
- while pay > 0: loops until amount is fully paid or overpaid
"""

pay = 50

while pay > 0:
    print(f"Amount Due: {pay}")
    try:
        payment = int(input("Insert Coin: "))
    except ValueError:
        print("Invalid coin value")
        continue
    if payment in {25, 10, 5}:
        pay -= payment
    else:
        print("Enter only (25, 10, 5) exchanges")

print(f"Change Owed: {abs(pay)}")
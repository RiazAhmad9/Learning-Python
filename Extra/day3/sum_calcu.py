"""
sum_calculator
-----------------
Keeps adding numbers until the user types 'done', then prints the total.

- total = 0: accumulator, starts at zero
- input() before try/except: lets us check for 'done' before attempting float()
- total += float(number): converts input and adds to running total in one step
- try/except ValueError: catches non-numeric input without crashing
- 'done' as exit: gives user control over when to stop
"""

total = 0
while True:
    number = input("Number: ")
    if number == "done":
        break
    try:
        total += float(number)
    except ValueError:
        print("Enter only numbers")

print(f"Sum: {total}")
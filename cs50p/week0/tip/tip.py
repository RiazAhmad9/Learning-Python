"""
tip.py
-----------------
Calculates the tip amount based on meal cost and tip percentage.

- dollars_to_float(): strips "$" and converts to float
- percent_to_float(): strips "%" and divides by 100 to get a decimal
- ValueError caught in main(): keeps conversion functions clean,
  handles bad input where it occurs
- 0 < percent <= 1: validates percentage is between 1 and 100 after conversion
- :.2f: formats tip to 2 decimal places
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    while True:
        try:
            dollars = dollars_to_float(input("How much was the meal? "))
            break
        except ValueError:
            print("Enter a valid amount")

    while True:
        try:
            percent = percent_to_float(input("Tip percentage: "))
            if not 0 < percent <= 1:
                print("Enter a percentage between 1 and 100")
                continue
            break
        except ValueError:
            print("Enter a valid percentage")

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    return float(dollars.strip("$"))

def percent_to_float(percent):
    return float(percent.strip("%")) / 100

if __name__ == "__main__":
    main()
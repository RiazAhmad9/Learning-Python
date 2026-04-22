# A simple calculator to calculate tip per meal.

# Function 'main' which takes user input and calculates the tip percent.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Defins dollars and strip '$' sign
def dollars_to_float(d):
    return float(d.strip("$"))

# Defins percent and strip '%' sign
def percent_to_float(p):
    return float(p.strip("%")) / 100

# Calls main again.
main()
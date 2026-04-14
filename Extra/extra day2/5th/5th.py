# Checks if a year is a leap year.

# Takes input from the user and checks if it is a valid input or not.
try:
    a = int(input("Enter a year: "))
except ValueError:
    print("Invalid input. Please enter a valid year.")
    exit()    

# Checks if the year is a leap year or not.
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")
# Leap year checker

# Stores valid input in 'a' variable
try:
    a = int(input("Enter a year: "))
# If input is invalid then prints error message and exits 
except (ValueError, NameError):
    print("Invalid input. Please enter a valid year.")
    exit()

# Checks if the year is a leap year and prints there for
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")
# Leap year checker

# 'try/except' so program doesn't crash
try:
    a = int(input("Enter a year: "))
except (ValueError, NameError):
    print("Invalid input. Please enter a valid year.")
    exit()

# '%' by 100 and 400 for exception years
if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")
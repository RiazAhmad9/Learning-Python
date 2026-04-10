# Calculating numbers

# Ask the user for two numbers
x = float(input("What's x? "))
y = float(input("What's y? "))


z = round(x / y, 3)

# sum of two numbers rounded to the nearest integer
print(f"{z:,}")
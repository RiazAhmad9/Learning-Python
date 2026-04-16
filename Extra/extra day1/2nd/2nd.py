# Basic Calculation(sum, diff, prod, div, rem) in Python

# Stores user input in (a, b, c) variable 
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Prints sum, diff, prod, div, rem and 'end' parameter to end the line after print
print(f"Sum = {a + b + c}\nDifference = {a - b - c}\n", end="")
print(f"Product = {a * b * c}\ndivision = {(a / b / c):.2f}\nRemainder = {a % b % c}")
# Basic Calculation(sum, diff, prod, div, rem)

# 'float' data type to store any fraction number
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# 'end' parameter to print at the end of the previous print and \n to print on the next line
print(f"Sum = {a + b + c}\nDifference = {a - b - c}\n", end="")
print(f"Product = {a * b * c}\ndivision = {(a / b / c):.2f}\nRemainder = {a % b % c}")
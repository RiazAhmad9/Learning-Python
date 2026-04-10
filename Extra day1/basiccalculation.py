# Basic Calculation(sum,diff,prod,div,avg,rem) in Python

#Ask the user for three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

#Calculate and print the sum, difference, product, quotient, average and remainder of the three numbers(use end=" " to print in the same line)
print(f"Sum = {a + b + c}, Difference = {a - b - c}, Product = {a * b * c}, Quotient = {a / b / c},", end=" ")
print(f"Average = {(a + b + c) / 3}, Remainder = {a % b % c}")

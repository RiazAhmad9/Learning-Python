# Simple calculator for (sum, diff, prod, div)

# Stores two number in (a, b) variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Stores operator from user in 'c' variable
c = input("Enter operator (+, -, *, /): ")

# Performs calculation based on operator
if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    result = a / b

# Prints result
print("Result: ", result)
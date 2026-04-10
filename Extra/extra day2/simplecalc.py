# Simple calculator program

# Takes two numbers from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Takes operator from user
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

# Prints the result
print("Result: ", result)
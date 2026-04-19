# Simple calculator for (sum, diff, prod, div)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = input("Enter operator (+, -, *, /): ")

# '+, -, *, /' operator to calculate
if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    result = a / b

print("Result: ", result)
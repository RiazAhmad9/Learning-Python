# Calculates two numbers with a arithmetic expression.

# User input.
text = input("Expression: ")

#Splits user input into variebles. 
x, y, z = text.split()
x, z = float(x), float(z)

# Determines calculation for arithmetic expresion.
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(f"{result:.1f}")

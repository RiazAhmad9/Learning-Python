# Multiplication table up to 10

# Stores input in 'n' variable
n = int(input("Number: "))

# Giving variable 'i' a starting value
i = 1

# Printing result until the condition meets
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

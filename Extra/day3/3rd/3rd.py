# Multiplication table up to 10

number = int(input("Number: "))
i = 1
# 'number * i' to print aslike a multiplication table
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

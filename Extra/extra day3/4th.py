# A simple sum calculator

# Giving the initial variable a fixed value.
total = 0

# Taking input until input is 'done' and calculating the sum.
while True:
    n = input("Number: ")
    if n == "done":
        break
    else:
        total += float(n)
        continue

# Printing total sum.
print(total)


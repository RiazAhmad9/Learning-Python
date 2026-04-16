# A simple (sum) calculator

# Seting variable 'total' initial value
total = 0

# Stores input in a loop until user inputs done and calculates the sum
while True:
    n = input("Number: ")
    if n == "done":
        break
    else:
        total += float(n)
        continue

# Prints total 
print(total)


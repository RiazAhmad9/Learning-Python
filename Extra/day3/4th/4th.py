# A simple (sum) calculator

total = 0
# while True to store input until user inputs done and calculates the sum
while True:
    number = input("Number: ")
    if number == "done":
        break
    else:
        total += float(number)
        continue

print(total)


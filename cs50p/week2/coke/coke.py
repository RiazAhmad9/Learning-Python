# Exchange machine

# Seting a starting value for 'i' variable
i = 50

# Loops around until condition meets
while i > 0:
    print("Amount Due:", i)
    n = int(input("Insert Coin: "))
    if n in [25, 10, 5]:
        i -= n

# Prints the absulate value of final result
print("Change Owed:", abs(i))
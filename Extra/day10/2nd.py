# Asking number between 1-10 in a loop

while True:
    try:
        number = int(input("Number(1-10): "))
        if 0 < number <= 10:
            break
        else:
            print("Must be between 1 and 10.")
    except ValueError:
        print("Enter a whole number")
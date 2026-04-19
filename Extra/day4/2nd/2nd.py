# Compares two number and prints the largest number

def main():
    x = float(input("First number: "))
    y = float(input("Second number: "))
    print("Largest number is", compare(x, y))

def compare(x, y):
    if x > y :
        number = x
        # if statement to print whole numbers as whole number
        if number == int(number):
            return int(number)
        else:
            return number
    else:
        number = y
        if number == int(number):
            return int(number)
        else:
            return number

if __name__ == "__main__":
    main()
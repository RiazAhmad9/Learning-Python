# Fuel gauge indicator.

# 'main' function which takes input in a loop until valid input, checks for error and prints the final result.
def main():
    while True:
        try:
            n = input("Fraction: ").split("/")
            x, y = int(n[0]), int(n[1])
            if x > y or y == 0:
                continue
            print(fuel(x, y))
            break
        except (ValueError, ZeroDivisionError):
            pass

# 'fuel' function which calculate the integers and convert them to specific answer considering the conditions. 
def fuel(x, y):
    p = round(x / y * 100)
    if p >= 99:
        return "F"
    elif p <= 1:
        return "E"
    else:
        return f"{p}%"
    
# Calls main.
main()
        
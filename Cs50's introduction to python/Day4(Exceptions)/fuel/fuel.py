# Fuel gauge indicator

# 'main' function which stores input, loops until valid input, checks for error and prints output
def main():
    while True:
        try:
            # Splits the string on '/'
            n = input("Fraction: ").split("/")
            # 'x, y' variable stores the splited values
            x, y = int(n[0]), int(n[1])
            # If conditions are right then prints else runs the loop again
            if x > y or y == 0 or x < 0 or y < 0:
                continue
            print(fuel(x, y))
            # breaks the loop after printing the output
            break
        # If error is found then runs the loop again
        except (ValueError, ZeroDivisionError):
            pass

# 'fuel' function which returns a answer considering the conditions
def fuel(x, y):
    # Calculation of fuel percentage is stored in 'p' variable
    p = round(x / y * 100)
    if p >= 99:
        return "F"
    elif p <= 1:
        return "E"
    else:
        return f"{p}%"
    
# Calls main
main()
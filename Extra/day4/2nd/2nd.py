# Compares two number

# 'main' function which stores input from user and prints the largest number
def main():
    x = float(input("First number: "))
    y = float(input("Second number: "))
    print("Largest number is", larger(x, y))

# Defined a function 'larger' to compare between two numbers
def larger(x, y):
    if x > y :
        # Sets variable 'result' value to 'x'
        result = x
        # Returns the value as int if it's a whole number else float
        if result == int(result):
            return int(result)
        else:
            return result
    else:
        # Sets variable 'result' value of 'y'
        result = y
        # Returns the value as int if it's a whole number else float
        if result == int(result):
            return int(result)
        else:
            return result

# Calls main
main()
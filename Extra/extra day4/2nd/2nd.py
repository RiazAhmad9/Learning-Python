# Compares two number.

# 'main' funstion which takes input from user and prints the largest number.
def main():
    x = float(input("First number: "))
    y = float(input("Second number: "))
    print("Largest number is", larger(x, y))

# Defined a function 'larger' to compare between two numbers.
def larger(x, y):
    if x > y :
        # Sets a variable 'result' to the value of 'x'.
        result = x
        # Returns the value as int if it is a whole number or float if its not.
        if result == int(result):
            return int(result)
        else:
            return result
    else:
        # Sets the variable'result' to the value of y.
        result = y
        # Returns the value as int if it is a whole number or float if its not.
        if result == int(result):
            return int(result)
        else:
            return result

# Calls main.
main()
# Prime number checker

# 'main' function that stores input in 'n' variable and prints final result
def main():
    n = int(input("Number: "))
    print(checker(n))

# Defined function 'checker' to check if it's a prime or not
def checker(x):
    # Verifies the integer 
    if x < 2:
        return "Not a valid number"
    # Checks the integer from value (2 to 'integer') and declares if it's a prime or not 
    for i in range(2, x):
        if x % i == 0:
            return "Not prime"
    return "Prime"
        
# Calls main
main()

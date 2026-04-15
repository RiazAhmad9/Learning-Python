# A number guessing game

# Imports a random integer and stores into 'secret_num' variable
import random
secret_num = random.randint(1, 100)

# 'checker' function where user input gets checked and an answer is returned
def checker(k):
    if k == secret_num :
        return "correct"
    elif k < secret_num :
        return "too low"
    elif k > secret_num :
        return "too high"

# 'main' function where user inserts a number and result gets print considering the conditions
def main():
    # Loop for the user to keep guessing number.
    while True:
        # If valid input is not found prints a specific message and continues the loop
        try:
            num = int(input("Guess a number (1-100): "))
        except ValueError:
            print("Enter a whole number.")
            continue
        # 'return' variable which stores the returned value from 'checker' function
        result = checker(num)
        # Prints conclusion
        print(result)
        # Breaks if conclusion is final else continues
        if result == "correct":
            break

# Calls main
if __name__ == "__main__":
    main()
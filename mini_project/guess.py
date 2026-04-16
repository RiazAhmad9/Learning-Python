# A number guessing game

# Imports a random number
import random

# 'checker' function where user input gets checked and an answer is returned
def checker(k, secret_num):
    if k == secret_num :
        return "correct"
    elif k < secret_num :
        return "too low\nTry again."
    elif k > secret_num :
        return "too high\nTry again."

# 'main' function where user inserts a number and result gets print considering the conditions
def main():
    # A random integer between (1-100) is stored in 'secret_num' variable
    secret_num = random.randint(1, 100)
    # Variable 'att' initial value to 0 to count user attempts
    att = 0
    # Variable 'max_att' value to 10 for limiting user attempts
    max_att = 10
    # Loop for the user to keep guessing number
    while True:
        # If valid input is not found prints a specific message and continues the loop
        try:
            num = int(input("Guess a number (1-100): "))
        except ValueError:
            print("Enter a whole number.")
            continue
        # Add 1 to 'att' variable
        att += 1
        # Breaks if 'att' is more than 'max_att'
        if att >= max_att:
            print(f"Out of guesses! The number is {secret_num}")
            break
        # 'return' variable which stores the returned value from 'checker' function
        result = checker(num, secret_num)
        # Prints conclusion
        print(result)
        # Breaks if conclusion is final else continues
        if result == "correct":
            # Prints how many attempts it took
            print(f"You took {att} guesses!")
            again = input("Play again? (y/n) ").lower()
            # If 'again' variable value is set to y then runs 'main()' again else breaks.
            if again == "y":
                main()
            elif again == "n":
                print("Thanks for playing!")
                break

# Calls main
if __name__ == "__main__":
    main()
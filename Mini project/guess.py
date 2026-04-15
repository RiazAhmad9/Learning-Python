# A number guessing game.

# 'main' function where user inserts a number and result gets print considering the conditions.
def main():
    # Loop for the user to keep guessing number.
    while True:
        num = int(input("Your Number: "))
        # Variable which stores the result from 'checker' function.
        result = checker(num)
        # Checks if answer is correct. If so then prints 'correct' else gives hint and asks for another number.
        if result == "correct":
            print(result)
            break
        else:
            print(result)
            continue

# Imports a random integer and stores into 'secret_num' variable.
import random
secret_num = random.randint(1, 100)   

# 'checker' function where users input gets checked and an answer is returned.
def checker(k):
    if k == secret_num :
        return "correct"
    elif k < secret_num :
        return "too low"
    elif k > secret_num :
        return "too high"

# Calls main.
main()
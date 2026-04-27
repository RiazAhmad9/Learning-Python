"""
number_guessing_game
-----------------------
A number guessing game where the player has 10 attempts to guess
a random number between 1 and 100.

- random.randint(1, 100): generates a new secret number each game
- checker(): separates guess evaluation from game loop logic
- att >= max_att: checked after result so the player always uses their last guess
- 1 <= num <= 100: chained comparison rejects out-of-range guesses
- play_again flag: signals the inner loop to break and the outer loop to restart
  with a fresh secret number and reset attempt counter
- return on "n": exits main() and terminates cleanly from any depth
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
import random


def checker(num, secret_num):
    if num == secret_num:
        return "correct"
    elif num < secret_num:
        return "too low\nTry again."
    elif num > secret_num:
        return "too high\nTry again."


def main():
    while True:
        secret_num = random.randint(1, 100)
        att = 0
        max_att = 10

        while True:
            try:
                num = int(input("Guess a number (1-100): "))
                if not 1 <= num <= 100:
                    print("Guess between 1 and 100")
                    continue
            except ValueError:
                print("Enter a whole number.")
                continue
            att += 1
            result = checker(num, secret_num)
            print(result)

            play_again = False
            if att >= max_att:
                print(f"Out of guesses! The number is {secret_num}")
                while True:
                    again = input("Play again? (Y/N) ").lower()
                    if again == "y":
                        play_again = True
                        break
                    elif again == "n":
                        print("Thanks for playing!")
                        return
                    else:
                        print("Select between (Y/N)")

            if result == "correct":
                print(f"You took {att} guesses!")
                while True:
                    again = input("Play again? (Y/N) ").lower()
                    if again == "y":
                        play_again = True
                        break
                    elif again == "n":
                        print("Thanks for playing!")
                        return
                    else:
                        print("Select between (Y/N)")
            if play_again:
                break

if __name__ == "__main__":
    main()
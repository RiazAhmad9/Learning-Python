'''
random.randint(a, b) generates a random integer between a and b, inclusive.

raise ValueError lets you manually trigger a ValueError, the same exception
that int() raises when it gets bad input. This lets you handle both cases
(bad type AND bad value) in a single except block.

continue skips the rest of the current loop iteration and jumps back to the top.
Used here to re-prompt when input is invalid, without running the guess logic.

exit() terminates the program immediately.
'''

import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            raise ValueError
        answer = random.randint(1, level)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            raise ValueError
    except ValueError:
        continue
    if guess == answer:
        print("Just right!")
        exit()
    elif guess < answer:
        print("Too small!")
    elif guess > answer:
        print("Too large!")

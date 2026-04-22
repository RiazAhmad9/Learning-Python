'''
get_level() prompts until the user inputs 1, 2, or 3.
raise ValueError lets us reject valid integers that are out of range,
handling both bad type and bad value in one except block.

generate_integer(level) returns one random number with the correct digit count.
  Level 1: 0–9, Level 2: 10–99, Level 3: 100–999
  min_val = 0 if level == 1 else 10 ** (level - 1)
  max_val = 10 ** level - 1

main() runs 10 problems, tracks score, and allows 3 attempts per problem.
  - att resets to 0 inside the for loop so each problem starts fresh.
  - ValueError on a bad guess is caught and re-prompts without incrementing att.
  - After 3 wrong attempts, the correct answer is shown and we break to the next problem.
  - score only increments on a correct answer.
'''

import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        att = 0
        x = generate_integer(level)
        y = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    att += 1
                if att == 3:
                    print(f"x + y = {x + y}")
                    att = 0
                    break
            except ValueError:
                continue
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
            else:
                raise ValueError
        except ValueError:
            continue

def generate_integer(level):
    min_val = 0 if level == 1 else 10 ** (level-1)
    max_val = 10 ** level - 1
    number = random.randint(min_val, max_val)
    return number


if __name__ == "__main__":
    main()
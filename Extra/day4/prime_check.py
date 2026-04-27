"""
prime_checker
----------------
Checks whether a given integer is a prime number.

- int(): primes are whole numbers, floats make no sense here
- while True + try/except: loops until valid input, catches non-numeric entries
- number < 2: primes are defined as greater than 1, rejects 0, 1, negatives
- range(2, int(number ** 0.5) + 1): only checks divisors up to square root —
  if no factor exists up to √n, none exist beyond it either (more efficient)
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    while True:
        try:
            number = int(input("Number: "))
            break
        except ValueError:
            print("Enter whole number")
    print(checker(number))

def checker(number):
    if number < 2:
        return "Not a valid number"
    for integer in range(2, int(number ** 0.5) + 1):
        if number % integer == 0:
            return "Not prime"
    return "Prime"

if __name__ == "__main__":
    main()
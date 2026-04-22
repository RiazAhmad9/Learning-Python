'''
is_valid() checks a vanity plate string against the following rules:
  1. Must be 2-6 characters long.
  2. Must start with at least two letters.
  3. Numbers cannot start with 0.
  4. Once a digit appears, no letters can follow.
  5. Only letters and digits are allowed — no spaces or punctuation.

number is a flag that tracks whether we have seen a digit yet.
Once number is True, any letter after it immediately returns False.
The flag starts as False and flips to True on the first digit encountered.

plate[0] and plate[1] directly index the first and second characters of the string.
isalpha() returns True if the character is a letter.
isdigit() returns True if the character is a digit.
'''

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    number = False
    for letter in plate:
        if letter.isdigit():
            if not number and letter == "0":
                return False
            number = True
        if number and letter.isalpha():
            return False
        if not letter.isalpha() and not letter.isdigit():
            return False
    return True

if __name__ == "__main__":
    main()
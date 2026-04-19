# Defines a plate number considering few rules

# 'main' function which shows the plate number either 'valid' or 'invalid'
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Defines the function 'is_valid'
def is_valid(s):
    # Checks if the string is between 2 and 6 letters
    if  len(s) < 2 or len(s) > 6:
        return False
    # Checks if first two character is an alphabet
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    # Sets variable 'digit' initial value to false
    digit = False
    # Initiates the loop to check for specific integers
    for i in s:
        # Checks if next character is a number
        if i.isdigit():
            # Checks if first integer is number '0'
            if not digit and i == "0":
                return False
            # If character is a number then changes 'digit' value to true
            digit = True
        # Checks digit value and if next character is a alphabet
        if digit and i.isalpha():
            return False
        # Checks if there's any other character rather than alphabet and numbers
        if not i.isalpha() and not i.isdigit():
            return False
    return True

# Calls main
main()
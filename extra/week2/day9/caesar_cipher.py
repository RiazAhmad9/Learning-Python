"""
caesar_cipher
----------------
Encodes a message using the Caesar cipher — shifts each letter
by a given number of positions in the alphabet.

- ord(letter) - ord("a"): converts letter to 0-25 range
- + shift: moves the letter forward by the shift amount
- % 26: wraps around if it goes past 'z'
- + ord("a"): converts back to ASCII range
- chr(): turns the number back into a letter
- preserves case: lowercase and uppercase handled separately
- non-letter characters (spaces, punctuation) are kept as-is
"""
result = ""
text = input("Secret message: ")

while True:
    try:
        shift = int(input("Shift: "))
        break
    except ValueError:
        print("Input a whole number")

for letter in text:
    if letter.isalpha():
        if letter.islower():
            result += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
    else:
        result += letter

print(result)
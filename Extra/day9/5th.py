# Caesar cipher which encodes a secret message

"""
ord(letter) - ord("a") → position in alphabet (0-25)
+ shift → move forward
% 26 → wrap around if past z
+ ord("a") → convert back to letter
chr() → turn that number into a letter
"""

text = input("Secret message: ")
while True:
    try:
        shift = int(input("Shift: "))
        break
    except ValueError:
        print("Input a integer")

result = ""
for letter in text:
    if letter.isalpha():
        if letter.lower():
            result += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
    else:
        result += letter

print(result)
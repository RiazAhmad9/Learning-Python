# Checking if a word is a palindrome(same letters for inverse)

text = input("Word: ")
text2 = text.lower()
# "[::-1]" used to reverse the order
if text2[::-1] == text2:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
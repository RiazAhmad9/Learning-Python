'''
Iterate over each character in the string one by one.
i.lower() normalizes the character to lowercase so we catch both 'A' and 'a'.
If the character is a vowel, we skip it by adding nothing to final.
If it's not a vowel, we concatenate it to final with +=.
This builds the filtered string character by character.
'''

text = input("Input: ")
final = ""

for i in text:
    if i.lower() not in ["a", "e", "i", "o", "u"]:
        final += i

print("Output:", final)

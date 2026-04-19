# Vowel and consonant counter

vowel_list = ["a", "e", "i", "o", "u"]
vowel = 0
consonant = 0
text = input("Sentence: ")
# 'for' loop to check every letter and statements to count only letters
for letter in text:
    if letter.isalpha():
        if letter.lower() in vowel_list:
            vowel += 1
        else:
            consonant += 1

print(f"Vowel = {vowel}\nConsonant = {consonant}")
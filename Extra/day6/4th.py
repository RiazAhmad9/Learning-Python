# character frequency
import string
def main():
    character = {} 
    text = sorted(input("Word: ").lower().strip())

    for letter in text:
        clean = letter.strip(string.punctuation)
        if not clean.isalpha():
            continue
        if clean in character:
            character[clean] = character[clean] + 1
        else:
            character[clean] = 1

    for i in character:
        print(f"{i} = {character[i]}")
            
            
if __name__ == "__main__":
    main()  


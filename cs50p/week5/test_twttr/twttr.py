'''
shorten() takes a string and returns it with all vowels removed.
Iterating over a string gives you one character at a time.
i.lower() normalizes to lowercase so we catch both 'A' and 'a'.
We only concatenate to final if the character is NOT a vowel.
This builds the filtered string character by character, then returns it.

if __name__ == "__main__" ensures main() only runs when the file is
executed directly, not when imported as a module by another file.
'''

def main():
    text = input("Input: ")
    print("Output:", shorten(text))


def shorten(word):
    final = ""
    for i in word:
        if i.lower() not in ["a", "e", "i", "o", "u"]:
            final += i
    return final


if __name__ == "__main__":
    main()
"""
caesar_cipher_class.py — OOP Fundamentals
===================================

Class:
    CaesarCipher(shift)

    Attributes:
        shift (int) — value to shift by

    Methods:
        encode() — shifts each letter forward by shift positions
        decode() — reverses encoding by shifting backward using -shift

Functions:
    get_option() — prompts user to choose encode or decode
    get_shift()  — prompts user for shift value, rejects non-integers

main():
    stores option and text, creates CaesarCipher, prints result
"""
class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift
    
    def encode(self, text):
        result = ""
        for letter in text:
            if letter.isalpha():
                if letter.islower():
                    result += chr((ord(letter) - ord("a") + self.shift) % 26 + ord("a"))
                else:
                    result += chr((ord(letter) - ord("A") + self.shift) % 26 + ord("A"))
            else:
                result += letter
        return result
    
    def decode(self, text):
        return CaesarCipher(-self.shift).encode(text)


def get_option():
    return input("1.Encode\n2.Decode\nSelect: ").lower()


def get_shift():
    while True:
        try:
            return int(input("Shift: "))
        except ValueError:
            print("Input a whole number")


def main():
    option = get_option()
    cipher = CaesarCipher(get_shift())
    text = input("Message: ")
    
    if option in ("1", "encode"):
        print(cipher.encode(text))
    elif option in ("2", "decode"):
        print(cipher.decode(text))
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
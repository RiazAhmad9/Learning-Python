"""
faces.py
------------------
Converts text emoticons into emoji characters.

- emoji.emojize(): converts emoji shortcodes like :slightly_smiling_face:
  into their actual emoji characters
- .replace(): substitutes each text emoticon with the corresponding emoji
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
import emoji

def main():
    text = input()
    print(convert(text))

def convert(text):
    text = text.replace(":)", emoji.emojize(":slightly_smiling_face:"))
    text = text.replace(":(", emoji.emojize(":slightly_frowning_face:"))
    return text

if __name__ == "__main__":
    main()
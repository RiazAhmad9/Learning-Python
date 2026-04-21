'''
Emoji converter
- Retries on empty input
- Lowercases only :alias: patterns, not regular words
- Tries alias names first (:smile:), falls back to CLDR (:grinning_face:)
- Warns if an alias wasn't recognised
'''
import re
import emoji

while True:
    text = input("Input: ")
    if not text:
        print("Try again")
    else:
        break

orginal = text
text = re.sub(r":\w+:", lambda match: match.group().lower(), text)
convert = emoji.emojize(text, language="alias")

if convert == text:
    convert = emoji.emojize(text)

if orginal == convert and re.search(r":\w+:", orginal):
    print("No emoji found")
else:
    print(convert)
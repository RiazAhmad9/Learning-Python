# Converting text emoji with icon emojis

# Imports all emoji icons.
import emoji

# Function 'main' where user gives input and prints converted input.
def main():
    user = input()
    print(convert(user))

# Function 'convert' where user input is converted.
def convert(text):
    text = text.replace(":)", emoji.emojize(":slightly_smiling_face:"))
    text = text.replace(":(", emoji.emojize(":slightly_frowning_face:"))
    return text

# Calls main again.
main()
    


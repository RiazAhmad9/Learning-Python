# Reversing word by word.

# Takes user input and prints the final output.
def main():
    text = input("Input: ")
    print("Output:", convert(text))

# 'convert' function splits input into strings, reverses them and glue them back together.
def convert(x):
    x = x.split()
    x.reverse()
    return " ".join(x)

# Calls main.
main()
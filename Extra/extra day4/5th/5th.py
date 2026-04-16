# Reversing word by word

# Stores user input in 'text' variable and prints the final output
def main():
    text = input("Input: ")
    print("Output:", convert(text))

# 'convert' function splits input into strings, reverses them and return them by gluing back together
def convert(x):
    x = x.split()
    x.reverse()
    return " ".join(x)

# Calls main
main()
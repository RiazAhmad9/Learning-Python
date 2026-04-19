# Reversing word by word

def main():
    text = input("Input: ")
    print("Output:", convert(text))

def convert(x):
    # 'split()' to split the string
    x = x.split()
    # 'reverse()' to invert strings
    x.reverse()
    # '" ".join()' to glue them back on whitespace
    return " ".join(x)

if __name__ == "__main__":
    main()
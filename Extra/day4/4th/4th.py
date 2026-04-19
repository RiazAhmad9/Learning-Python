# Temp convert system

# 'main' for option, storeing value and printing
def main():
    choice = input("Please choose (C/F): ").lower().strip()
    if choice == "c":
        number = float(input("C: ").strip())
        # ':.2f' to print only point two decimal
        print(f"F: {cels_to_fahr(number):.2f}\u00b0")
    elif choice == "f":
        number = float(input("F: ").strip()) 
        print(f"C: {fahr_to_cels(number):.2f}\u00b0")

def cels_to_fahr(f):
    f = ((f * (9/5)) + 32)
    return f

def fahr_to_cels(c):
    c = ((c - 32) * (5/9))
    return c

if __name__ == "__main__":
    main()

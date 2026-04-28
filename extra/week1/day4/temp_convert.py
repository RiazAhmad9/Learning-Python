"""
temp_converter
-----------------
Converts temperature between Celsius and Fahrenheit based on user choice.

- cels_to_fahr(number): applies formula (n * 9/5) + 32
- fahr_to_cels(number): applies formula (n - 32) * 5/9
- choice not in [...]: validates input against all accepted options in one check
- .lower().strip(): normalises input, handles capitalisation and whitespace
- :.2f + \u00b0: formats result to 2 decimal places with degree symbol
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def cels_to_fahr(number):
    return (number * (9/5)) + 32

def fahr_to_cels(number):
    return (number - 32) * (5/9)

def main():
    while True:
        choice = input("Please choose\n1.Celsius\n2.Fahrenheit\nSelect: ").lower().strip()
        if choice not in ["1", "2", "celsius", "fahrenheit"]:
            print("Choose between 2 options")
            continue
        break
    if choice == "celsius" or choice == "1":
        while True:
            try:
                number = float(input("Celsius: "))
                break
            except ValueError:
                print("Enter only numbers")
        print(f"Fahrenheit: {cels_to_fahr(number):.2f}\u00b0")
    elif choice == "fahrenheit" or choice == "2":
        while True:
            try:
                number = float(input("Fahrenheit: "))
                break
            except ValueError:
                print("Enter only numbers")
        print(f"Celsius: {fahr_to_cels(number):.2f}\u00b0")

if __name__ == "__main__":
    main()
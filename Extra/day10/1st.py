# Simple calculator(error handling practice)

def main():
    while True:
        while True:
            try:
                a = float(input("Enter first number: "))
                break
            except ValueError:
                print("Please enter only numbers")

        while True:
            try:
                b = float(input("Enter second number: "))
                break
            except ValueError:
                print("Please enter only numbers")

        while True:
            o = input("Operator(+, -, *, /): ").strip()
            if o == "+":
                result = a + b
                break
            elif o == "-":
                result = a - b
                break
            elif o == "*":
                result = a * b
                break
            elif o == "/":
                if b == 0:
                    print("Can't divide by zero")
                    continue
                result = a / b
                break
            else:
                print("Please enter a valid operator")

        print("Result:", result)
        while True:
            select = input("1.Quit\n2.Continue\nSelect: ").lower().strip()
            if select == "1" or select == "quit":
                return
            elif select == "2" or select == "continue":
                pass
            else:
                print("Please select from provided options")

if __name__ == "__main__":
    main()
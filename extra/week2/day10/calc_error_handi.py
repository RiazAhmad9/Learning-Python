"""
calculator_with_error_handling
----------------------------------
A simple calculator with full input validation and error handling.

- three separate input loops: isolates validation for each input (a, b, operator)
- float(): accepts decimals, raises ValueError on non-numeric input
- b == 0 check inside "/" case: catches division by zero before it happens
- continue inside operator loop: re-prompts operator without re-asking numbers
- return on quit: exits main() and terminates the program cleanly
- break on continue: exits the quit/continue loop and restarts the outer loop
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

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
        print(f"Result: {result}")

        while True:
            select = input("1.Quit\n2.Continue\nSelect: ").lower().strip()
            if select == "1" or select == "quit":
                return
            elif select == "2" or select == "continue":
                break
            else:
                print("Please select from provided options")

if __name__ == "__main__":
    main()
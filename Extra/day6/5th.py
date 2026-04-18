# Option system with the help of dictonary
option = {"1": "Say Hello",
          "2": "Add two numbers",
          "3": "Quit",
          }

def main():
    while True:
        try:
            text = input("Option(1-3): ")
            if text in option:
                print(option[text])
            else:
                print("Invalid input")
            if text == "3":
                break
        # control-d or control-z to exit
        except EOFError:
            break



if __name__ == "__main__":
    main()
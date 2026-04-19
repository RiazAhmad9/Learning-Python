# Prime number checker

def main():
    number = int(input("Number: "))
    print(checker(number))

def checker(x):
    # if statement to handle exceptions 
    if x < 2:
        return "Not a valid number"
    # for loop to set a range for cheking
    for i in range(2, x):
        if x % i == 0:
            return "Not prime"
    return "Prime"
        
if __name__ == "__main__":
    main()

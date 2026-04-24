'''
1.datetime module to import todays date.
2.'main' function to take input in lowercase and run runction as chosen.
3.'read_diary' to print the file line by line with '.rstrip'.
4.'write_diary' to append present date and input line by line and exits with input 'done done'.
5.At the end if function so code doesn't run by itself until called.
'''
from datetime import date

def main():
    while True:
        option = input("Diary:\n1.Open\n2.Write\n3.Close\nSelect: ").lower()
        if option == "1" or option == "open":
            read_diary()
        elif option == "2" or option == "write":
            write_diary()
        elif option == "3" or option == "close":
            break

def read_diary():
    try:
        with open("3rd.txt", "r") as file:
            for text in file:
                print(text.rstrip())
    except FileNotFoundError:
        print("Diary not found")

def write_diary():
    date_diary = date.today()
    with open("3rd.txt", 'a') as file:
        file.write(f"{date_diary}\n")
        while True:
            text = input("Type 'done done' to exit\nInput: ")
            if text == "done done":
                break
            file.write(f"{text}\n")

if __name__ == "__main__":
    main()
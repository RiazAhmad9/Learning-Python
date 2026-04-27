"""
diary
--------
A simple diary app that reads and appends entries to a text file.

- from datetime import date: imports only what's needed for date.today()
- read_diary(): opens diary.txt in read mode, prints line by line with .rstrip()
  to remove trailing newlines — catches FileNotFoundError if file is missing
- write_diary(): opens in append mode, writes today's date then user input
  line by line — catches PermissionError on open() where it would actually occur
- 'done done' as exit: two words to avoid accidental exit on 'done' alone
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

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
        else:
            print("Invalid option")


def read_diary():
    try:
        with open("diary.txt", "r") as file:
            for text in file:
                print(text.rstrip())
    except FileNotFoundError:
        print("Diary not found")


def write_diary():
    date_diary = date.today()
    try:
        with open("diary.txt", "a") as file:
            file.write(f"{date_diary}\n")
            while True:
                text = input("Type 'done done' to exit\nInput: ")
                if text == "done done":
                    break
                file.write(f"{text}\n")
    except PermissionError:
        print("Permission denied — cannot write to file")


if __name__ == "__main__":
    main()
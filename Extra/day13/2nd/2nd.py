'''
1.Opens a ".txt file if available else closes with a error message.
2."r" argument to read the file.
3.Number and name variable to set numbers beside names while sorting them.
4.Number starts with 1 rather than 0.
5.Strips the empty line from print.
'''

try:
    with open("1st.txt", "r") as file:
        for number, name in enumerate(sorted(file), 1):
            print(f"{number}.{name.rstrip()}")
except FileNotFoundError:
    print("File not found")
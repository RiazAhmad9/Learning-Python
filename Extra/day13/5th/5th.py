'''
1.'readlines' to store the file into a list to sort it before writing it in another file.
2.'w' instead of 'a' to overwrite the file.
'''

try:
    with open("names.txt", "r") as file:
        names = file.readlines()
        names = sorted(names)
        with open("sorted_names.txt", "w") as file:
            for name in names:
                file.write(f"{name.strip()}\n")
except FileNotFoundError:
    print("File not found")
# Trying to open a file without crashing

filename = input("Filename: ").strip()
try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print(f"{filename} not found")
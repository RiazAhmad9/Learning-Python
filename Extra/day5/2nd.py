# Sorting names alphabetically

def main():
    names = []
    # while True ensures invalid input re-promts insted of skipping
    while True: 
        try:
            name = input("Name: ").title().strip()
            if name.replace(" ", "").isalpha():
                names.append(name)
            else:
                print("Names should only contain letters")
        # EOFError to break the loop by inputing 'control-z' or 'control-d'
        except EOFError:
            break
    # for lop to number, sort alphabetically and pass same name only once
    for i, name in enumerate(sorted(set(names)), 1):
        print(f"{i}.{name}")

if __name__ == "__main__":
    main() 

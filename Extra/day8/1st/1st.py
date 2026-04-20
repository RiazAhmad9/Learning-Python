# Phone dictonary

import json
# File where contacts are stored
FILE = "contacts.json"
# Loads contacts from FILE or returns empty dictonary on startup
def load():
    try:
        with open(FILE, 'r') as contacts_file:
            return json.load(contacts_file)
    except FileNotFoundError:
        return {}
    
def save():
    try:
        with open(FILE, "w") as contacts_file:
            json.dump(contacts, contacts_file)
    except OSError:
        print("Could not save contacts")
        
contacts = load()

def add():
    while True:
        name = input("Name: ").lower().strip()
        if name.replace(" ", "").isalpha():
            break
        print("Name should only contain letters, try again")

    if name in contacts:
        choice = input(f"{name.title()} already exist ({contacts[name]}). Update? (Y/N): ").lower()
        if choice != "y":
            return
    
    while True:
        number = input(f"Number({name.title()}): ").strip()
        if number.isdigit() and 1 <= len(number) <= 15:
            if number in contacts.values():
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name] = number
            print("Saved")
            save()
            break
        print("Enter a valid phone number (1-15 digits only)")

def lookup():
    name = input("Name: ").lower().strip()
    if name in contacts:
        print(f"Number({name.title()}):", contacts[name])
    else:
        print("Name not found")

def delete():
    name = input("Name: ").lower().strip()
    if name in contacts:
        del contacts[name]
        print("Deleted")
        save()
    else:
        print("Name not found")

def contact_list():
    if not contacts:
        print("No contacts saved")
        return
    for name, number in sorted(contacts.items()):
        print(f"{name.title()}: {number}")

def main():
    while True:
        option = input("1:Add\n2:Lookup\n3:Delete\n4:List\n5:Quit\nOption: ").lower().strip()
        if option == "add" or option == "1":
            add()
        elif option == "lookup" or option == "2":
            lookup()
        elif option == "delete" or option == "3":
            delete()
        elif option == "list" or option == "4":
            contact_list()
        elif option == "quit" or option == "5":
            break
        else:
            print("Not a valid option")

if __name__ == "__main__":
     main()
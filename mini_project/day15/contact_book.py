import json
import re

"""
Contact Book — CLI phonebook application
=========================================
Data is stored in 'contact_book.json' as a nested dictionary:
    {"name": {"number": "412...", "email": "user@example.com"}}
Both number and email are optional, but at least one must be provided.

FUNCTIONS:
----------
load()
    Reads contact_book.json and returns contacts dict.
    Returns empty dict if file is missing or corrupted (FileNotFoundError,
    json.JSONDecodeError both handled).
    Called once at startup inside __main__ block.

save()
    Writes the current contacts dict to contact_book.json.
    Called after any change (add, update, delete).
    Catches OSError if file write fails.

add()
    Adds a new contact or updates an existing one.
    - Name: letters, spaces, hyphens, apostrophes only (regex validated)
    - Number: international format supported, min 7 digits, max 15 characters
              (optional, press Enter to skip)
    - Email: must have content before @, valid domain, dot in domain (optional)
    - Warns if number or email already exists (user can override)
    - Rejects if both number and email are skipped

search()
    Looks up a contact by exact name match.
    Prints name, number, and email if found.

update()
    Updates number and/or email for an existing contact.
    Shows current info before prompting.
    Rejects if name not found.
    Skipping a field (pressing Enter) leaves it unchanged.
    Number and email validation identical to add().

show_list()
    Prints all contacts sorted alphabetically.
    Shows name, number, and email for each entry.

delete()
    Deletes a contact by exact name match.
    Prints confirmation or not-found message.

main()
    Main loop. Accepts numeric (1-6) or keyword input (add, search, etc.)

KNOWN LIMITATIONS:
------------------
- Names are stored lowercase, displayed with .title()
- No support for multiple numbers or emails per contact
- No partial search — lookup and delete require exact name match
- Number duplicate check compares raw strings — +61412711 and 412711
  are treated as different numbers even if they resolve to the same line
"""


FILE = "contact_book.json"
contacts = {}

def load():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return{}

def save():
    try:
        with open(FILE, "w") as file:
            json.dump(contacts, file)
    except OSError:
        print("Failed to save")

def add():
    while True:
        name = input("Name: ").lower().strip()
        if re.match(r"^[a-zA-Z\s'\-]+$", name):
            break
        print("Names must contain only letters")
    if name in contacts:
        choice = input(f"{name.title()} already exist\nNumber: {contacts[name]['number']}\nEmail: {contacts[name]['email']}\nUpdate? (Y/N): ").lower()
        if choice != "y":
            return
    else:
        contacts[name] = {"number": None, "email": None}

    while True:
        number = input("Number: ").strip()
        if number == "":
            break
        if re.match(r"^\+?[\d\s\-\(\)]{7,15}$", number) and sum(contact.isdigit() for contact in number) >= 7:
            if any(contact["number"] == number for contact in contacts.values()):
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name]["number"] = number
            print("Saved")
            break
        print("Enter a valid phone number (3-15 digits only)")

    while True:
        email = input("Email: ").strip().lower()
        if email == "":
            break
        parts = email.split("@")
        if parts[0] != "" and len(parts) == 2:
            domain_parts = parts[1].split(".")
            if domain_parts[0] != "" and domain_parts[-1] != "" and len(domain_parts) >= 2:
                if any(contact["email"] == email for contact in contacts.values()):
                    choice = input("Email already exist. Save anyway? (Y/N): ").lower()
                    if choice != "y":
                        return
                contacts[name]["email"] = email
                print("Saved")
                break
        print("Enter a valid email")

    if contacts[name]["number"] is None and contacts[name]["email"] is None:
        print("Must provide at least one contact method")
        del contacts[name]
        return
    save()

def search():
    name = input("Name: ").lower().strip()
    if name in contacts:
        print(f"Name: {name.title()}\nNumber: {contacts[name]['number']}\nEmail: {contacts[name]['email']}")
    else:
        print("Name not found")

def update():
    name = input("Name: ").lower().strip()
    if name not in contacts:
        print("Name not found")
        return
    print(f"Current —\nNumber: {contacts[name]['number']}\nEmail: {contacts[name]['email']}")
    while True:
        number = input("Phone: ").strip()
        if number == "":
            break
        if re.match(r"^\+?[\d\s\-\(\)]{7,15}$", number) and sum(contact.isdigit() for contact in number) >= 7:
            if any(contact["number"] == number for contact in contacts.values()):
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name]["number"] = number
            print("Updated")
            break

    while True:
        email = input("Email: ").strip().lower()
        if email == "":
            break
        parts = email.split("@")
        if parts[0] != "" and len(parts) == 2:
            domain_parts = parts[1].split(".")
            if len(domain_parts) >= 2 and domain_parts[0] != "" and domain_parts[-1] != "":
                if any(contact["email"] == email for contact in contacts.values()):
                    choice = input("Email already exist. Save anyway? (Y/N): ").lower()
                    if choice != "y":
                        return
                contacts[name]["email"] = email
                print("Updated")
                break
    save()

def show_list():
    if not contacts:
        print("No contacts saved")
        return
    for name, contact in sorted(contacts.items()):
        print(f"Name: {name.title()}\nNumber: {contact['number']}\nEmail: {contact['email']}")

def delete():
    name = input("Name: ").lower().strip()
    if name in contacts:
        del contacts[name]
        print("Deleted")
        save()
    else:
        print("Name not found")

def main():
    while True:
        option = input("1.Add\n2.Search\n3.Update\n4.List\n5.Delete\n6.Close\nSelect: ").lower()
        if option == "1" or option == "add":
            add()
        elif option == "2" or option == "search":
            search()
        elif option == "3" or option == "update":
            update()
        elif option == "4" or option == "list":    
            show_list()
        elif option == "5" or option == "delete":
            delete()
        elif option == "6" or option == "close":
            break
        else:
            print("Please select between (1-6)")

if __name__ == "__main__":
    contacts = load()
    main()
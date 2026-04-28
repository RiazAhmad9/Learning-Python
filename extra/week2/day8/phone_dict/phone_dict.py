"""
phone_dict.py — Terminal-based phonebook application.

Stores contacts as name-number pairs in a local JSON file (phone_dict.json).
Supports adding, looking up, deleting, and listing contacts with input
validation and duplicate detection.

Modules:
    json — Handles persistent storage via phone_dict.json
    re   — Validates name and phone number input formats

Global:
    contacts (dict): In-memory store of {name (str): number (str)} pairs.
                     Initialized as {} at module level, populated by load()
                     at startup, and written back to disk on each change.

Functions:
    load()         -> dict  : Reads phone_dict.json into a dict.
                              Returns {} if file is missing or JSON is corrupt.
    save()                  : Writes the global contacts dict to phone_dict.json.
                              Prints an error message on OSError.
    add()                   : Prompts for a name and number with validation loops.
                              Handles duplicate names (update prompt) and
                              duplicate numbers (save-anyway prompt).
    lookup()                : Finds and prints a contact by exact name match.
    delete()                : Removes a contact by name and saves to disk.
    contact_list()          : Prints all contacts sorted alphabetically by name.
    main()                  : Menu loop. Accepts numeric (1-5) or text input.

Validation rules:
    Names   — Letters, spaces, apostrophes, hyphens only (regex).
    Numbers — Optional leading +, then digits/spaces/dashes/parentheses,
              3–15 characters total (regex).

Usage:
    python phone_dict.py

Limitations:
    - One number per contact (adding updates the existing entry).
    - No partial/fuzzy name search; lookup requires an exact name match.
    - Number duplicate check compares raw strings — +8801711 and 01711
      are treated as different numbers even if they resolve to the same line.
"""
import json
import re

FILE = "phone_dict.json"
contacts = {}

def load():
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    

def save():
    try:
        with open(FILE, "w") as file:
            json.dump(contacts, file)
    except OSError:
        print("Could not save")


def add():
    while True:
        name = input("Name: ").lower().strip()
        if re.match(r"^[a-zA-Z\s'\-]+$", name):
            break
        print("Names must contain only letters")
    if name in contacts:
        choice = input(f"{name.title()} already exist-\nNumber: {contacts[name]}\nUpdate? (Y/N): ").lower()
        if choice != "y":
            return
    
    while True:
        number = input("Number: ").strip()
        if re.match(r"^\+?[\d\s\-\(\)]{3,15}$", number):
            if number in contacts.values():
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name] = number
            print("Saved")
            save()
            break
        print("Enter a valid phone number (3-15 digits only)")


def lookup():
    name = input("Name: ").lower().strip()
    if name in contacts:
        print(f"{name.title()}: {contacts[name]}")
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
    contacts = load()
    main()
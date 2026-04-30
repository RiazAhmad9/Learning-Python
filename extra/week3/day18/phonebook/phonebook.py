"""
phonebook.py — Terminal-based phonebook application (OOP refactor).

Stores contacts as name-number pairs in a local JSON file (phone_dict.json).
Supports adding, looking up, deleting, and listing contacts with input
validation and duplicate detection.

Modules:
    json — Handles persistent storage via phone_dict.json
    re   — Validates name and phone number input formats

Classes:
    Contact(name, number)
        Attributes:
            name   (str) — contact's name
            number (str) — contact's phone number

    Phonebook()
        Attributes:
            contacts (dict) — in-memory store of {name: number} pairs
        Methods:
            load()         — reads phone_dict.json into self.contacts
            save()         — writes self.contacts to phone_dict.json
            add()          — prompts for name/number with validation;
                             handles duplicates
            lookup()       — finds and prints a contact by exact name
            delete()       — removes a contact by name and saves
            contact_list() — prints all contacts sorted alphabetically

Validation rules:
    Names   — Letters, spaces, apostrophes, hyphens only (regex).
    Numbers — Optional leading +, then digits/spaces/dashes/parentheses,
              3–15 characters total (regex).

Usage:
    python phonebook.py

Limitations:
    - One number per contact (adding updates the existing entry).
    - No partial/fuzzy name search; lookup requires exact name match.
    - Number duplicate check compares raw strings — +8801711 and 01711
      are treated as different numbers even if they resolve to the same line.
    - Contact class is defined but not yet used for storage.
"""
import json
import re
FILE = "phone_dict.json"


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Phonebook:
    def __init__(self):
        self.contacts = {}
    
    def load(self):
        try:
            with open(FILE, 'r') as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = {}
        
    def save(self):
        try:
            with open(FILE, "w") as file:
                json.dump(self.contacts, file)
        except OSError:
            print("Could not save")

    def add(self):
        while True:
            name = input("Name: ").lower().strip()
            if re.match(r"^[a-zA-Z\s'\-]+$", name):
                break
            print("Names must contain only letters")
        
        if name in self.contacts:
            choice = input(f"{name.title()} already exist-\nNumber: {self.contacts[name]}\nUpdate? (Y/N): ").lower()
            if choice != "y":
                return
            
        while True:
            number = input("Number: ").strip()
            if re.match(r"^\+?[\d\s\-\(\)]{3,15}$", number):
                if number in self.contacts.values():
                    choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                    if choice != "y":
                        return
                self.contacts[name] = number
                print("Saved")
                self.save()
                break
            print("Enter a valid phone number (3-15 digits only)")

    def lookup(self):
        name = input("Name: ").lower().strip()

        if name in self.contacts:
            print(f"{name.title()}: {self.contacts[name]}")
        else:
            print("Name not found")
        
    def delete(self):
        name = input("Name: ").lower().strip()

        if name in self.contacts:
            del self.contacts[name]
            print("Deleted")
            self.save()
        else:
            print("Name not found")
    
    def contact_list(self):
        if not self.contacts:
            print("No contacts saved")
            return
        
        for name, number in sorted(self.contacts.items()):
            print(f"{name.title()}: {number}")


def main():
    phonebook = Phonebook()
    phonebook.load()

    while True:
        option = input("1:Add\n2:Lookup\n3:Delete\n4:List\n5:Quit\nOption: ").lower().strip()
        if option == "add" or option == "1":
            phonebook.add()
        elif option == "lookup" or option == "2":
            phonebook.lookup()
        elif option == "delete" or option == "3":
            phonebook.delete()
        elif option == "list" or option == "4":
            phonebook.contact_list()
        elif option == "quit" or option == "5":
            break
        else:
            print("Not a valid option")


if __name__ == "__main__":
    main()
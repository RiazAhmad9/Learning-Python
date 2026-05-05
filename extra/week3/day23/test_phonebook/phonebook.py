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
        Methods:
            __str__() — returns "name: number" formatted string

    Phonebook()
        Attributes:
            contacts (list) — in-memory list of Contact objects
        Methods:
            load()    — reads phone_dict.json into self.contacts;
                        initializes empty list if file missing or corrupt
            save()    — serializes self.contacts to phone_dict.json
            add()     — appends a Contact object and saves
            lookup()  — returns Contact by case-insensitive name match,
                        or None if not found
            delete()  — removes Contact by name and saves;
                        prints "Name not found" if no match
            __str__() — returns all contacts sorted alphabetically,
                        or "No contacts found" if list is empty
            valid_name()  — returns True if name contains only letters, spaces,
                apostrophes, or hyphens
            valid_number() — returns True if number contains 7-15 digits and
                            matches expected phone format

Validation rules (enforced via static methods):
    Names   — Letters, spaces, apostrophes, hyphens only (regex).
    Numbers — Must contain 7-15 digits (non-digit characters excluded
              from count). Format allows optional leading + with country
              code, area codes in parentheses, and digits separated by
              spaces or dashes.

Usage:
    python phonebook.py

Limitations:
    - One number per contact; adding an existing name prompts to update.
    - No partial/fuzzy name search; lookup requires exact name match.
    - Number duplicate check compares raw strings — +8801711 and 01711
      are treated as different numbers even if they resolve to the same line.
"""
import json
import re
FILE = "phone_dict.json"


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Phonebook:
    def __init__(self):
        self.contacts = []

    def __str__(self):
        if not self.contacts:
            return "No contacts found"
        contact_list = []
        for contact in sorted(self.contacts, key=lambda n: n.name):
            contact_list.append(str(contact))
        return "\n".join(contact_list)

    def load(self):
        try:
            with open(FILE, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(n["name"], n["number"]) for n in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []

    def save(self):
        try:
            with open(FILE, "w") as file:
                json.dump([{"name": n.name, "number": n.number} for n in self.contacts], file)
        except OSError:
            print("Could not save")

    def add(self, contact):
        self.contacts.append(contact)
        self.save()
        print("Added")

    def lookup(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def delete(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.save()
                print("Removed")
                return
        print("Name not found")
    
    @staticmethod
    def valid_name(name):
        return bool(re.match(r"^[a-zA-Z\s'\-]+$", name))

    @staticmethod
    def valid_number(number):
        digits = len(re.sub(r"\D", "", number))
        return 7 <= digits <= 15 and bool(re.fullmatch(r"(?:\+\d{1,3}[\s\-\.]|\(\d{2,3}\)?[\s])?\d+(?:[\s\-\.]?\d+)*", number))


def main():
    phonebook = Phonebook()
    phonebook.load()

    while True:
        option = input("1:Add\n2:Lookup\n3:Delete\n4:List\n5:Quit\nOption: ").lower().strip()
        if option == "add" or option == "1":
            while True:
                name = input("Name: ").strip()
                if Phonebook.valid_name(name):
                    break
                print("Names must contain only letters")
            existing = phonebook.lookup(name)
            if existing:
                choice = input(f"{name.title()} already exists.\nNumber: {existing.number}\nUpdate? (Y/N): ").lower()
                if choice != "y":
                    continue
                while True:
                    number = input("New number: ").strip()
                    if Phonebook.valid_number(number):
                        existing.number = number
                        phonebook.save()
                        print("Updated")
                        break
                    print("Invalid number (7-15 digits required)")
                continue
            while True:
                number = input("Number: ").strip()
                if Phonebook.valid_number(number):
                    number_exists = any(c.number == number for c in phonebook.contacts)
                    if number_exists:
                        choice = input("Number already exists. Save anyway? (Y/N): ").lower()
                        if choice != "y":
                            break
                    contact = Contact(name, number)
                    phonebook.add(contact)
                    break
                else:
                    print("Invalid number (7-15 digits required)")

        elif option == "lookup" or option == "2":
            while True:
                try:
                    name = input("Name: ").strip()
                    if name == "":
                        raise ValueError("Missing name")
                    break
                except ValueError as n:
                    print(n)
            result = phonebook.lookup(name)
            if result:
                print(result)
            else:
                print("Name not found")

        elif option == "delete" or option == "3":
            while True:
                try:
                    name = input("Name: ").strip()
                    if name == "":
                        raise ValueError("Missing name")
                    break
                except ValueError as n:
                    print(n)
            phonebook.delete(name)

        elif option == "list" or option == "4":
            print(phonebook)

        elif option == "quit" or option == "5":
            break

        else:
            print("Not a valid option")


if __name__ == "__main__":
    main()
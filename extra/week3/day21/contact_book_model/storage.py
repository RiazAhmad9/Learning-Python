'''
Storage — handles reading and writing contacts to contact_book.json.

Data is stored as:
    {"name": {"number": "412...", "email": "user@example.com"}}

load()  — reads file and returns {name: Contact} dict.
          returns empty dict if file is missing or corrupted.
save()  — converts Contact objects to dicts and writes to file.
          catches OSError if file write fails.
'''
import json
from models import Contact
FILE = "contact_book.json"


def load():
    try:
        with open(FILE, "r") as file:
            raw = json.load(file)
            raw = {name: Contact.from_dict(name, data) for name, data in raw.items()}
            return raw
    except (FileNotFoundError, json.JSONDecodeError):
        return{}


def save(contacts):
    try:
        with open(FILE, "w") as file:
            data = {name: contact.to_dict() for name, contact in contacts.items()}
            json.dump(data, file)
    except OSError:
        print("Failed to save")
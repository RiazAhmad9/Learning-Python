'''
Contact — data model for a single contact entry.

Stores name, number, and email as attributes.
Number and email are optional but at least one must be provided.

to_dict()       — converts contact to plain dict for JSON serialisation
from_dict()     — builds a Contact from a name and dict loaded from JSON
valid_name()    — returns True if name contains only letters, spaces, hyphens, apostrophes
valid_number()  — returns True if number matches phone format with at least 7 digits
valid_email()   — returns True if email matches a realistic address pattern
'''
import re

class Contact:
    def __init__(self, name, number=None, email=None):
        self.name = name
        self.number = number
        self.email = email

    def to_dict(self):
        return {"number": self.number, "email": self.email}
    
    @classmethod
    def from_dict(cls, name, data):
            return cls(name, data["number"], data["email"])
    
    @staticmethod
    def valid_name(name):
        return bool(re.match(r"^[a-zA-Z\s'\-]+$", name))

    @staticmethod
    def valid_number(number):
        return (bool(re.match(r"^\+?[\d\s\-\(\)]{7,15}$", number)) and 
                sum(c.isdigit() for c in number) >= 7)

    @staticmethod
    def valid_email(email):
        return bool(re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email))
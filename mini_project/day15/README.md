# Contact Book

A command-line phonebook that stores contacts locally in a JSON file.

## Usage

Run the app:
```bash
python contact_book.py
```

You'll see a menu:
1.Add
2.Search
3.Update
4.List
5.Delete
6.Close
Select by number (1-6) or keyword (add, search, update, list, delete, close).

---

## Features

**Add** — Save a new contact with a name, phone number, and/or email.
- At least one of number or email is required.
- Warns if a number or email already exists.

**Search** — Look up a contact by exact name.

**Update** — Edit the number or email of an existing contact.
- Press Enter to skip a field and leave it unchanged.

**List** — Display all contacts sorted alphabetically.

**Delete** — Remove a contact by exact name.

---

## Notes

- Data is saved automatically to `contact_book.json` in the same directory.
- Names are case-insensitive — "Ali" and "ali" are the same contact.
- Partial search is not supported — use the exact name.
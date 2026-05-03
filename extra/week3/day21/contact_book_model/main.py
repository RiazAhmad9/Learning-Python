'''
Main — CLI interface for the contact book.

add(contacts)       — prompts for name, number, email and saves a new contact.
                      warns if number or email already exists, rejects if both skipped.
search(contacts)    — looks up a contact by exact name match and prints details.
update(contacts)    — finds a contact and overwrites number or email. skipping a
                      field leaves it unchanged.
show_list(contacts) — prints all contacts sorted alphabetically.
delete(contacts)    — removes a contact by exact name match and saves.
main()              — loads contacts and runs the menu loop. accepts numeric (1-6)
                      or keyword input.

known limitations:
    names stored lowercase, displayed with .title()
    no partial search — requires exact name match
    no support for multiple numbers or emails per contact
'''
import re
from storage import load, save
from models import Contact


def add(contacts):
    while True:
        name = input("Name: ").lower().strip()
        if Contact.valid_name(name):
            break
        print("Names must contain only letters")
    if name in contacts:
        choice = input(f"{name.title()} already exist\nNumber: {contacts[name].number}\nEmail: {contacts[name].email}\nUpdate? (Y/N): ").lower()
        if choice != "y":
            return
    else:
        contacts[name] = Contact(name)

    while True:
        number = input("Number: ").strip()
        if number == "":
            break
        if Contact.valid_number(number):
            if any(c.number == number for c in contacts.values()):
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name].number = number
            print("Saved")
            break
        print("Enter a valid phone number (3-15 digits only)")

    while True:
        email = input("Email: ").strip().lower()
        if email == "":
            break
        if Contact.valid_email(email):
            if any(c.email == email for c in contacts.values()):
                choice = input("Email already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name].email = email
            print("Saved")
            break
        print("Enter a valid email")

    if contacts[name].number is None and contacts[name].email is None:
        print("Must provide at least one contact method")
        del contacts[name]
        return
    save(contacts)


def search(contacts):
    name = input("Name: ").lower().strip()
    if name in contacts:
        print(f"Name: {name.title()}\nNumber: {contacts[name].number}\nEmail: {contacts[name].email}")
    else:
        print("Name not found")


def update(contacts):
    name = input("Name: ").lower().strip()
    if name not in contacts:
        print("Name not found")
        return
    print(f"Current —\nNumber: {contacts[name].number}\nEmail: {contacts[name].email}")
    while True:
        number = input("Phone: ").strip()
        if number == "":
            break
        if Contact.valid_number(number):
            if any(c.number == number for c in contacts.values()):
                choice = input("Number already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name].number = number
            print("Updated")
            break

    while True:
        email = input("Email: ").strip().lower()
        if email == "":
            break
        if Contact.valid_email(email):
            if any(c.email == email for c in contacts.values()):
                choice = input("Email already exist. Save anyway? (Y/N): ").lower()
                if choice != "y":
                    return
            contacts[name].email = email
            print("Updated")
            break
    save(contacts)


def show_list(contacts):
    if not contacts:
        print("No contacts saved")
        return
    for name, contact in sorted(contacts.items()):
        print(f"Name: {name.title()}\nNumber: {contact.number}\nEmail: {contact.email}")


def delete(contacts):
    name = input("Name: ").lower().strip()
    if name in contacts:
        del contacts[name]
        print("Deleted")
        save(contacts)
    else:
        print("Name not found")


def main():
    contacts = load()

    while True:
        option = input("1.Add\n2.Search\n3.Update\n4.List\n5.Delete\n6.Close\nSelect: ").lower()
        if option == "1" or option == "add":
            add(contacts)
        elif option == "2" or option == "search":
            search(contacts)
        elif option == "3" or option == "update":
            update(contacts)
        elif option == "4" or option == "list":    
            show_list(contacts)
        elif option == "5" or option == "delete":
            delete(contacts)
        elif option == "6" or option == "close":
            break
        else:
            print("Please select between (1-6)")


if __name__ == "__main__":
    main()
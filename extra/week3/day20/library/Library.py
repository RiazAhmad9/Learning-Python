"""
Library.py — Terminal-based library application (OOP refactor).

Stores books as title-author in a local JSON file (library_list.json).
Supports adding, looking up, removing, and listing books with input
validation.

Modules:
    json — Handles persistent storage via library_list.json
    re   — Validates author's name input formats

Classes:
    Book(title, author)
        Attributes:
            title   (str) — book's title
            author (str) —  book's author
        Methods:
            __str__() — returns "title by author" formatted string

    Library()
        Attributes:
            books (list) — in-memory store of {title by author}
        Methods:
            load()         — reads library_list.json into self.books
            save()         — writes self.books to library_list.json
            __str__()      — retunrs all book as a sorted, formatted string
            add()          — prompts for title and author with validation
            search()       — finds and prints a book by exact title
            remove()       — removes a book by title and saves

Validation rules:
    author   — Letters, spaces, apostrophes, hyphens only (regex).

Limitations:
    - No partial/fuzzy title search; search requires exact title match.
    - No duplicate checker
"""
import json
import re
FILE = "library_list.json"


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def __str__(self):
        book_list = []
        if not self.books:
            return "No books in library"
        
        for book in sorted(self.books, key=lambda b: b.title):
            book_list.append(str(book))
        return "\n".join(book_list)

    def load(self):
        try:
            with open(FILE, 'r') as file:
                data = json.load(file)
                self.books = [Book(b["title"], b["author"]) for b in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
        
    def save(self):
        try:
            with open(FILE, "w") as file:
                json.dump([{"title": b.title, "author": b.author} for b in self.books], file)
        except OSError:
            print("Could not save")

    def add(self, book):
        self.books.append(book)
        self.save()
        print("Added")

    def search(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def remove(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save()
                print("Removed")
                return
        print("Book not found")

 
def main():
    library = Library()
    library.load()

    while True:
        option = input("1:Add\n2:Search\n3:Remove\n4:List\n5:Quit\nOption: ").lower().strip()

        if option == "add" or option == "1":
            while True:
                try:
                    title = input("Title: ")
                    if title == "":
                        raise ValueError("Missing title")
                    break
                except ValueError as t:
                    print(t)
            
            while True:
                try:
                    author = input("Author: ")
                    if author == "":
                        raise ValueError("Missing author")
                    if re.match(r"^[a-zA-Z\s'\-]+$", author):
                        break
                    print("Invalid name format")
                except ValueError as a:
                    print(a)
            
            book = Book(title, author)
            library.add(book)
        
        elif option == "search" or option == "2":
            while True:
                try:
                    title = input("Title: ")
                    if title == "":
                        raise ValueError("Missing title")
                    break
                except ValueError as t:
                    print(t)
            
            result = library.search(title)
            if result:
                print(result)
            else:
                print("Book not found")

        elif option == "remove" or option == "3":
            while True:
                try:
                    title = input("Title: ")
                    if title == "":
                        raise ValueError("Missing title")
                    break
                except ValueError as t:
                    print(t)
            
            library.remove(title)

        elif option == "list" or option == "4":
            print(library)
        
        elif option == "quit" or option == "5":
            break

        else:
            print("Not a valid option")


if __name__ == "__main__":
    main()
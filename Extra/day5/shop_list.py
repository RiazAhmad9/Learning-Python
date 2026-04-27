"""
shopping_list
----------------
Collects items into a list until user types 'done', then prints all items.

- items = []: local list to store entries
- .lower(): normalises input so 'Done', 'DONE' etc. all trigger the exit
- .capitalize(): stores items with first letter capitalised for clean output
- 'done' as exit: gives user control over when to stop
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    items = []
    while True:
        item = input("Item: ").lower()
        if item == "done":
            for item in items:
                print(item)
            break
        items.append(item.capitalize())

if __name__ == "__main__":
    main()
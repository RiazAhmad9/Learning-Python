# Shopping list
def main():
    items = []
    while True:
        text = input("Item: ").lower()
        # Check before appending so 'done' stays out of the list
        if text == "done":
            for item in items:
                print(item)
            break
        # Capitalize for cosistent formatting
        items.append(text.capitalize())

if __name__ == "__main__":
    main()
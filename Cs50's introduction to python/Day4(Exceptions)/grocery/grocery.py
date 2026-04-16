# Grocery list

# 'main' function where list gets sorted, numbered and printed alphabetically in uppercase
def main():
    # 'item' dictonary to store values later on
    items = {}
    # Loops until user is done and count them as well with the help of dictonary
    while True:
        try:
            text = input().lower().strip()
            # Considering the condition statement adds '1' to the item from dictonary
            if text in items:
                items[text] = items[text] + 1
            else:
                items[text] = 1
            continue
        # Breaks the loop and prints the final list if user inputs 'control-z' or 'control-d'
        except EOFError:
            # Sorts the items by alphabet
            for i in sorted(items):
                # Prints the sorted items in uppercase
                print (items[i], i.upper())
            # Breaks the loop
            break

# Calls main
main()
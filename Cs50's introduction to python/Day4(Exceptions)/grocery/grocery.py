# Grocery list.

# 'main' function where list get sorted, numbered and printed in alphabetically in uppercase.
def main():
    # 'item' dictonary initial value.
    items = {}
    # Loop for taking input until user is finished and count them as well with the help of dictonary.
    while True:
        try:
            text = input().lower().strip()
            if text in items:
                items[text] = items[text] + 1
            else:
                items[text] = 1
            continue
        # Breaks the loop and prints the final list if user inputs 'control-z' or 'control-d'.
        except EOFError:
            # Sorts the items by alphabet.
            for i in sorted(items):
                # Prints the sorted items in uppercase.
                print (items[i], i.upper())
            break

# Calls main.
main()




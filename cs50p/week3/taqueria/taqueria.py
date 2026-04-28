"""
taqueria.py
-----------
Calculates a running total for a taqueria order until EOF (Ctrl+D / Ctrl+Z).

- price dict: maps menu items to their prices, defined globally above functions
- .lower().strip(): normalises input — handles case and whitespace
- total(): returns price if item is in dict, None otherwise
- result is not None: silently ignores invalid items, only adds valid ones
- total_cost += result: accumulates running total
- EOFError: raised when user signals end of input, exits the loop
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
price = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}


def main():
    total_cost = 0
    while True:
        try:
            order = input("Item: ").lower().strip()
            result = total(order)
            if result is not None:
                total_cost += result
                print(f"Total: ${total_cost:.2f}")
        except EOFError:
            break


def total(key):
    if key in price:
        return price[key]


if __name__ == "__main__":
    main()
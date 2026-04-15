# Felipe’s Taqueria menu price calculator.

# Defined main function.
def main():
    # Stores a initial value.
    total_cost = 0
    # Loops until the user is done and prints the total price each time.
    while True:
        # Checks for valid input.
        try:
            order = input("Item: ").lower().strip()
            # Stores the price from dictionary.
            result = total(order)
            # If result is valid prints the total_cost and add's it to total_cost.
            if result is not None:
                total_cost += result
                print(f"Total: ${total_cost:.2f}")
            continue
        # Stops the loop if user inputs 'control-z' or 'control=d'.
        except EOFError:
            break

# 'total' function which checks if input is in dictionary and returns the value.
def total(key):
    if key in price:
        return price[key]

# Price dictionary.
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

# Calls main.
main()
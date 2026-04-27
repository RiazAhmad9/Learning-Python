"""
compare_two_numbers
----------------------
Compares two numbers and prints the largest, or notes if they are equal.

- float(): accepts decimals, raises ValueError on non-numeric input
- while True + try/except: loops until valid input
- if/elif/else: covers all three cases — first larger, second larger, or equal
- int(n) if n == int(n): prints whole numbers without decimals (e.g. 5 not 5.0)
- round(n, 2): limits decimal output to 2 places for cleaner display
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    while True:
        try:
            first = float(input("First number: "))
            second = float(input("Second number: "))
            break
        except ValueError:
            print("Enter only numbers")
    compare(first, second)

def compare(first, second):
    if first > second:
        print(f"Largest is {int(first) if first == int(first) else round(first, 2)}")
    elif second > first:
        print(f"Largest is {int(second) if second == int(second) else round(second, 2)}")
    else:
        print("Numbers are equal")

if __name__ == "__main__":
    main()
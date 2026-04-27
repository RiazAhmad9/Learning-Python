"""
even_from_two_lists
----------------------
Combines two lists, removes duplicates, and prints even numbers in sorted order.

- list_1 + list_2: merges both lists into one
- set(): removes duplicates from the combined list
- sorted(): returns a sorted list from the set
- number % 2 == 0: checks if number is evenly divisible by 2
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [5, 6, 8, 6, 9]
    numbers = sorted(set(list_1 + list_2))
    for number in numbers:
        if number % 2 == 0:
            print(number)

if __name__ == "__main__":
    main()
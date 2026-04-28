"""
stats_calculator
-------------------
Collects 5 numbers and prints the lowest, highest, and average.

- numbers = []: local list to store inputs, defined inside main() not globally
- for _ in range(5): loops exactly 5 times, _ signals the variable is unused
- .append(): adds each valid input to the list
- min() / max(): built-ins that return smallest and largest values in a list
- sum() / len(): used together to calculate the average
- :.2f: formats average to 2 decimal places
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def calc(number):
    return f"Lowest = {min(number)}\nHighest = {max(number)}\nAverage = {(sum(number) / len(number)):.2f}"

def main():
    numbers = []
    for _ in range(5):
        while True:
            try:
                number = float(input("Number: "))
                numbers.append(number)
                break
            except ValueError:
                print("Enter only numbers")
    print(calc(numbers))

if __name__ == "__main__":
    main()
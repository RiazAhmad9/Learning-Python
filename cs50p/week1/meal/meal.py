"""
meal.py
------------
Converts a time input (HH:MM) and prints the corresponding meal time.

- convert(): splits time string on ":" and converts to a float
  e.g. "7:30" → 7.5
- int(time[0]) + (int(time[1]) / 60): converts minutes to decimal hours
- ValueError caught in main(): handles non-numeric or malformed input
- exit(): terminates cleanly after invalid input
- if/elif/else: covers breakfast (7-8), lunch (12-13), dinner (18-19),
  and anything outside those ranges
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    time = input("What time is it? ")
    try:
        time = convert(time)
    except ValueError:
        print("Invalid format")
        exit()
    if 7.0 <= time <= 8.0:
        print("Breakfast time")
    elif 12.0 <= time <= 13.0:
        print("Lunch time")
    elif 18.0 <= time <= 19.0:
        print("Dinner time")
    else:
        print("Not right time yet")


def convert(time):
    time = time.split(":")
    return int(time[0]) + (int(time[1]) / 60)


if __name__ == "__main__":
    main()
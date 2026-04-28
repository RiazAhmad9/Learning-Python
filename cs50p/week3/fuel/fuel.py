"""
fuel.py
-------------
Converts a fraction (X/Y) to a fuel gauge reading.

- convert(): splits "X/Y", validates, returns percentage rounded to nearest int
  raises ZeroDivisionError if Y is 0
  raises ValueError if X > Y or either is negative
- gauge(): returns "E" if <= 1%, "F" if >= 99%, otherwise "Z%"
- main(): handles input and re-prompts silently on ValueError or ZeroDivisionError
- separating convert() and gauge() from main(): keeps logic pure and testable with pytest
- if __name__ == "__main__": ensures main() only runs when executed directly
"""

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0:
        raise ValueError
    return round(x / y * 100)

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
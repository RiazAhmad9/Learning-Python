'''
convert() takes a string in "X/Y" format, splits it on "/", and converts
both parts to integers. It raises ZeroDivisionError if Y is 0, and
ValueError if X is greater than Y or either is negative. Returns the
fraction as a percentage rounded to the nearest int.

gauge() takes an int and returns "E" if <= 1, "F" if >= 99, or "Z%" otherwise.
It only handles the display logic — no input or calculation happens here.

main() handles all user input and re-prompts on ValueError or ZeroDivisionError.
Separating convert() and gauge() from main() keeps logic testable —
pure functions with no input/output are easy to test with pytest.

if __name__ == "__main__" ensures main() only runs when the file is
executed directly, not when imported as a module by another file.
'''

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
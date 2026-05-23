from datetime import date
import inflect
import sys

def main():
    print(minutes_to_word(conv(input("Date of Birth: "))))


def conv(s):
    try:
        dob = date.fromisoformat(s)
        if dob > date.today():
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid date")
    sub = date.today() - dob
    return sub.days * 24 * 60

def minutes_to_word(m):
    p = inflect.engine()
    return f"{p.number_to_words(m, andword = '')} minutes"


if __name__ == "__main__":
    main()
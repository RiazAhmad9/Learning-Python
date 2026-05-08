import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    extract = re.fullmatch(r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s)
    if extract:
        h1, m1, p1, h2, m2, p2 = extract.groups()
        start = time_convert(int(h1), int(m1) if m1 else 0, p1)
        end = time_convert(int(h2), int(m2) if m2 else 0, p2)
        return f"{start} to {end}"
    raise ValueError

def time_convert(hour, minute, period):
    if hour > 12 or minute > 59:
        raise ValueError
    elif period == "AM" and hour == 12:
        hour = 0
    elif period == "PM" and hour != 12:
        hour += 12
    return f"{hour:02d}:{minute:02d}"

if __name__ == "__main__":
    main()
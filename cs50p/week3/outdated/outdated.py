"""
outdated.py
-----------------
Converts a date in MM/DD/YYYY or "Month DD, YYYY" format to YYYY-MM-DD.

- months dict: maps month names to numbers for word-format parsing
- two branches in final_date(): handles "/" format and word format separately
- "/" branch: all values are raw strings — day, month, year all validated
- word branch: month comes from dict lookup — KeyError handles invalid names,
  so no range check needed; day and year still validated
- zfill(2): pads month and day with leading zero if needed (e.g. 1 → 01)
- ValueError / IndexError / KeyError caught in main(): silently re-prompts
  on any invalid input
- if __name__ == "__main__": ensures main() only runs when executed directly
"""
months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def main():
    while True:
        date = input("Date: ").strip().lower()
        try:
            print(final_date(date))
            break
        except (ValueError, IndexError, KeyError):
            pass


def final_date(date):
    if "/" in date:
        date = date.split("/")
        day = date[1]
        if not 1 <= int(day) <= 31:
            raise ValueError
        month = date[0]
        if not 1 <= int(month) <= 12:
            raise ValueError
        year = date[2]
        if not 1 <= int(year) <= 9999:
            raise ValueError
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    else:
        date = date.split(" ")
        if not date[1].endswith(","):
            raise ValueError
        day = date[1].strip(",")
        if not 1 <= int(day) <= 31:
            raise ValueError
        month = months[date[0]]
        year = date[2]
        if not 1 <= int(year) <= 9999:
            raise ValueError
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"


if __name__ == "__main__":
    main()
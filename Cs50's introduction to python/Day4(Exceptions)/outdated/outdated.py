# Computer date system

# 'monts' dictonary to set a value for each month
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

# 'main' function for user to input in a loop until valid input and prints the final date
def main():
    while True:
        # Stores input in 'user' variable
        user = input("Date: ").strip().lower()
        try:
            # Prints output
            print(f"{final_date(user)}")
            # Breaks the loop
            break
        # If error is found then loop continues
        except (ValueError, IndexError, KeyError):
            pass

#'final_date' function which outputs the result 
def final_date(date):
    # For input with '/'
    if "/" in date:
        # Splits the input on '/'
        date = date.split("/")
        # Sets the 'day' variable the value of 2nd index
        day = date[1]
        # Checks if the 'day' variable value is among (1-31)
        if int(day) < 1 or int(day) > 31:
            raise ValueError
        # Sets the 'month' variable the value of 1st index
        month = date[0]
        # Checks if the 'month' variable value is among (1-12)
        if int(month) < 1 or int(month) > 12:
            raise ValueError
        # Sets the 'year' variable the value of 3rd index
        year = date[2]
        # Returns the values as instructed and 'zfill' parameter to fill with '0'
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
    # For input with ' ' and ','
    else:
        # Splits the input on ' '
        date = date.split(" ")
        # Reject if comma is missing
        if not date[1].endswith(","):
            raise ValueError
        # Strips the index[1] from ',' and sets the 'day' variable the value of 2nd index
        day = date[1].strip(",")
        # Checks if the 'day' variable value is among 1-31
        if int(day) < 1 or int(day) > 31:
            raise ValueError
        # Sets the 'month' variable the value of 1st index
        month = months[date[0]]
        # Checks if the 'month' variable value is among 1-12
        if int(month) < 1 or int(month) > 12:
            raise ValueError
        # Sets the 'year' variable the value of 3rd index
        year = date[2]
        # Returns the values as instructed
        return f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"

# Calls main
main()
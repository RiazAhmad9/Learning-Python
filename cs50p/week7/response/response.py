import validators

def main():
    print(valid_email(input("What's your email address? ")))


def valid_email(e):
    if validators.email(e):
        return "Valid"
    return "Invalid"

if __name__ == "__main__":
    main()
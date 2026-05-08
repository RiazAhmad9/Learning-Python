import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    validation =  re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
    if validation:
        return all(0 <= int(number) <= 255 for number in validation.groups())
    return False


if __name__ == "__main__":
    main()
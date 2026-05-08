import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if url:
        return f"https://youtu.be/{url.group(1)}"
    return None


if __name__ == "__main__":
    main()
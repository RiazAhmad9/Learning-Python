"""
Name cleaner using regex.

Pattern breakdown:
- Name: 1. Filters number with the help of (re.sub) by replacing numbers with a space
        2. Remove multiple spaces with help of split()
        3. title() helps with upper and lower case

- Limitations: Doesn't work for names aslike (McDonald,MacGregor)
"""
import re


def name_clean(name):
    name = re.sub(r"\d+", " ", name)
    clean_name = name.strip().split()
    final_name = " ".join(clean_name)
    return f"{final_name.title()}"
    
def main():
    name = input("Name: ")
    print(name_clean(name))

if __name__ == "__main__":
    main()
"""
Name cleaner using regex.

Pattern breakdown:
- Name: 1. Filters number with the help of (re.sub) by replacing numbers with a space
        2. Remove multiple spaces with help of split()
        3. title() helps with upper and lower case

- Limitations: Doesn't work for names aslike (McDonald,MacGregor)
"""
import re
names = ["  john   doe  ", "JOHN DOE", "  jOhN   dOe  ", "john doe", "john123doe", "O'brien", "mcdonald"]

for name in names:
    name = re.sub(r"\d+", " ", name)
    clean_name = name.strip().split()
    final_name = " ".join(clean_name)
    print(final_name.title())
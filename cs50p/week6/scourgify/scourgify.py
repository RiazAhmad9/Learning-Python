"""
scourgify.py

Reads a CSV file with 'name' and 'house' columns, splits the name into
first and last, and writes a new CSV with 'first', 'last', and 'house' columns.

Usage: python scourgify.py <input.csv> <output.csv>
Exits with an error if arguments are invalid or if the input file does not exist.
"""
import sys, csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as infile, open(sys.argv[2], "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        data = []
        for row in reader:
            last, first = row["name"].split(",")
            data.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(data)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
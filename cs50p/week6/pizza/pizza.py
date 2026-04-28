"""
pizza.py

Reads a CSV file in Pinocchio's Pizza format and outputs the data
as an ASCII art table using the tabulate library.

Usage: python pizza.py <filename.csv>
Exits with an error if arguments are invalid, file is not .csv, or file does not exist.
"""
import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        table = csv.DictReader(file)
        print(tabulate(table, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File not found")
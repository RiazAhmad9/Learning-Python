"""
lucky_number.py
===============

How it works:
    creates a file saved as today's date if it doesn't exist 
    and prints a random number in it with today' date. Shows 
    the same lucky number if user prints it again.

    If file exists → reads and print it. if not → generate number, write and print it.

os:
    - 'BASE' strips the filename, leavinjg just the folder
    - 'FOLDER' builds a path by joining the folder with "lucky_numbers"
    - 'os.makedirs' creates the folder and stops from crashing if it exists
    - 'FILE' builds the full file path

datetime:
    - imports today's date

random:
    - gets a random integer between 1 and 100
"""
from datetime import date
import random
import os

BASE = os.path.dirname(__file__)
FOLDER = os.path.join(BASE, "lucky_numbers")
os.makedirs(FOLDER, exist_ok=True)
FILE = os.path.join(FOLDER, f"{date.today()}.txt")


number = random.randint(1, 100)
try:
    with open(FILE, "r") as file:
        print(file.read())
except FileNotFoundError:
    with open(FILE, "w") as file:
        file.write(f"{date.today()}\n{number}")
        print(f"Your lucky number today is {number}")    

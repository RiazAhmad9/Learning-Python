import csv

name = input("Whta's your name? ")
home = input("What's your home? ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
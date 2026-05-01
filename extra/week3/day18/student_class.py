"""
Student Class — OOP Fundamentals
=================================
Demonstrates a basic class with attributes and a method.

Class:
    Student(name, grade)
        Attributes:
            self.name  (str) — student's name
            self.grade (int) — score between 0 and 100
        Method:
            pass_fail() → returns "Pass" (grade >= 60) or "Fail" (grade < 60)

Usage:
    student = Student("Riaz", 75)
    print(student.pass_fail())  # → Pass

Validation:
    - Empty name raises ValueError
    - Grade validated in main() to be int between 0-100
"""
class Student:
    def __init__(self, name, grade):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.grade = grade

    def pass_fail(self):
        if 0 <= self.grade < 60:
            return "Fail"
        elif 60 <= self.grade <= 100:
            return "Pass"
 

def main():
    name = input("Name: ")
    while True:
        try:
            grade = int(input("Score: "))
            if not 0 <= grade <= 100:
                raise ValueError
            break
        except ValueError:
            print("Enter a number between 0-100")
    student = Student(name, grade)
    print(f"{student.name}: {student.pass_fail()}")


if __name__ == "__main__":
    main()
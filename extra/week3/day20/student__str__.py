"""
Student Class — OOP Fundamentals __str__
=================================

Class:
    Student(name, grade)
        Attributes:
            self.name  (str) — student's name
            self.grade (int) — score between 0 and 100
        Method:
            pass_fail() → returns "Pass" (grade >= 60) or "Fail" (grade < 60)
            __str__()   → returns student name with pass or fail string

Validation:
    - Empty name reprompts with error message
    - Grade validated in main() to be int between 0-100
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def pass_fail(self):
        if 0 <= self.grade < 60:
            return "Fail"
        elif 60 <= self.grade <= 100:
            return "Pass"
        
    def __str__(self):
        return f"{self.name}: {self.pass_fail()}"
 

def main():
    while True:
        try:
            name = input("Name: ")        
            if not name:
                raise ValueError("Missing name")
            break
        except ValueError as n:
            print(n)
    while True:
        try:
            grade = int(input("Score: "))
            if not 0 <= grade <= 100:
                raise ValueError("Enter a number between 0-100")
            break
        except ValueError as g:
            print(g)
    student = Student(name, grade)
    print(student)


if __name__ == "__main__":
    main()
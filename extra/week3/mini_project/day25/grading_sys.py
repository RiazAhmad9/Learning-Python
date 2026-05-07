import json
import re
FILE = "student_list.json"


class Student:
    def __init__(self, name):
        self.name = name
        self.score = []

    def __str__(self):
        avg = self.average()
        return f"Student: {self.name}\nScores: {self.score}\nAverage: {avg}\nGrade: {self.grade(avg)}\nStatus: {self.status(avg)}"

    def average(self):
        try:
            return sum(self.score) / len(self.score)
        except ZeroDivisionError:
            return 0
    
    @staticmethod
    def grade(average):
        if average >= 93:
            return "4.0(A)"
        elif average >= 90 and average < 93:
            return "3.7(A-)"
        elif average >= 87 and average < 90:
            return "3.3(B+)"
        elif average >= 83 and average < 87:
            return "3.0(B)"
        elif average >= 80 and average < 83:
            return "2.7(B-)"
        elif average >= 77 and average < 80:
            return "2.3(C+)"
        elif average >= 73 and average < 77:
            return "2.0(C)"
        elif average >= 70 and average < 73:
            return "1.7(C-)"
        elif average >= 67 and average < 70:
            return "1.3(D+)"
        elif average >= 60 and average < 67:
            return "1.0(D)"
        elif average < 60:
            return "0.0(F)"
    
    @staticmethod
    def status(average):
        if average >= 60:
            return "Pass"
        elif average < 60:
            return "Fail"
        
    @staticmethod
    def valid_name(name):
        if not name.strip():
            return False
        return bool(re.fullmatch(r"[a-z\s'\-]+", name, re.IGNORECASE))


class Student_list:
    def __init__(self):
        self.student = []

    def __str__(self):
        if not self.student:
            return "No student data saved"
        students = []
        for student in sorted(self.student, key=lambda s: s.name):
            students.append(str(student))
        return "\n".join(students)
    
    def load(self):
        try:
            with open(FILE, "r") as file:
                student_data = json.load(file)
                for s in student_data:
                    student = Student(s["name"])
                    student.score = s["score"]
                    self.student.append(student)
        except (FileNotFoundError, json.JSONDecodeError):
            self.student = []

    def save(self):
        try:
            with open(FILE, "w") as file:
                json.dump([{"name": s.name, "score": s.score} for s in self.student], file)
        except (OSError):
            print("Could not save")

    def add_student(self, name):
        student = Student(name)
        self.student.append(student)
        self.save()
        print("Added")
        return student

    def view_report(self, name):
        for student in self.student:
            if student.name.lower() == name.lower():
                return student
        return None
    
    def delete_student(self, name):
        for student in self.student:
            if student.name.lower() == name.lower():
                self.student.remove(student)
                self.save()
                print("Deleted")
                return
        print("Student not found")


def main():
    student_list = Student_list()
    student_list.load()

    while True:
        option = input("1.Add-student\n2.Add-score\n3.Update-score\n4.View-report\n5.View-full-list\n6.Delete-student\n7.Quit\nSelect any option number: ").lower().strip()
        
        if option in ["1", "add-student", "add student", "addstudent"]:
            while True:
                name = input("Student name: ").strip()
                if Student.valid_name(name):
                    break
                print("Invalid name format")
            existing = student_list.view_report(name)
            if existing:
                choice = input(f"{name} already exist\nUpdate score? (Y/N)\nSelect: ").lower().strip()
                if choice != "y":
                    continue
                existing.score = []
                while True:
                    try:
                        try:
                            score = int(input("Score: "))
                            if 0 <= score <= 100:
                                existing.score.append(score)
                                print("(Ctrl-z)/(ctrl-d) to stop")
                            else:
                                raise ValueError
                        except ValueError:
                            print("Enter only numbers between 0-100")
                    except EOFError:
                        student_list.save()
                        break
            else:
                new_student = student_list.add_student(name)
                add_choice = input("Add score now? (Y/N)\nSelect: ").lower().strip()
                if add_choice in ["y", "yes"]:
                    while True:
                        try:
                            try:
                                score = int(input("Score: "))
                                if 0 <= score <= 100:
                                    new_student.score.append(score)
                                    student_list.save()
                                    print("(Ctrl-z)/(ctrl-d) to stop")
                                else:
                                    raise ValueError
                            except ValueError:
                                print("Enter only numbers between 0-100")
                        except EOFError:
                            break
                else:
                    continue
            
        elif option in ["2", "add-grade", "add grade", "addgrade"]:
            while True:
                name = input("Student name: ").strip()
                if Student.valid_name(name):
                    existing = student_list.view_report(name)
                    if existing:
                        while True:
                            try:
                                try:
                                    score = int(input("Score: "))
                                    if 0 <= score <= 100:
                                        existing.score.append(score)
                                        print("(Ctrl-z)/(ctrl-d) to stop")
                                    else:
                                        raise ValueError
                                except ValueError:
                                    print("Enter only numbers between 0-100 ")
                            except EOFError:
                                student_list.save()
                                break
                    else:
                        print("Student not found")
                    break
                else:
                    print("Invalid name format")

        elif option in ["3", "update-grade", "update grade", "updategrade"]:
            while True:
                name = input("Student name: ").strip()
                if Student.valid_name(name):
                    break
                print("Invalid name format")
            existing = student_list.view_report(name)
            if existing:
                existing.score = []
                while True:
                    try:
                        try:
                            score = int(input("Score: "))
                            if 0 <= score <= 100:
                                existing.score.append(score)
                                print("(Ctrl-z)/(ctrl-d) to stop")
                            else:
                                raise ValueError
                        except ValueError:
                            print("Enter only numbers between 0-100")
                    except EOFError:
                        student_list.save()
                        break
            else:
                print("Student not found")

        elif option in ["4", "view-report", "view report", "viewreport"]:
            while True:
                name = input("Student name: ").strip()
                if Student.valid_name(name):
                    report = student_list.view_report(name)
                    if report:
                        print(report)
                    else:
                        print("Student not found")
                    break
                else:
                    print("Invalid name format")

        elif option in ["5", "view-full-list", "view full list", "viewfulllist"]:
            print(student_list)

        elif option in ["6", "delete-student", "delete student", "deletestudent"]:
            while True:
                name = input("Student name: ").strip()
                if Student.valid_name(name):
                    student_list.delete_student(name)
                    break
                else:
                    print("Invalid name format")
        
        elif option in ["7", "quit", "exit", "stop"]:
            break
        
        else:
            print("Not a valid option")


if __name__ == "__main__":
    main()
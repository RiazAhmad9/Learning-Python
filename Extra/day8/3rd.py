# Grading stored value in a dictonary

grades = {
    "Student_1" : 50,
    "Student_2" : 35,
    "Student_3" : 75,
}


for name, grade in grades.items():
    print(name, "Pass" if grade >= 50 else "Fail")


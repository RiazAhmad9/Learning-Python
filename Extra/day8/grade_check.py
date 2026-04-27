"""
grade_checker
----------------
Checks whether each student in a dictionary has passed or failed.

- grades.items(): returns each key-value pair as (name, grade)
- ternary operator: concise single-line if/else for simple conditions
- pass threshold: 50 or above is a pass
"""

grades = {
    "Student_1": 50,
    "Student_2": 35,
    "Student_3": 75,
}

for name, grade in grades.items():
    print(name, "Pass" if grade >= 50 else "Fail")
# Grading System

score = float(input("Enter the score: "))

if score >= 93:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 87:
    grade = "B+"
elif score >= 83:
    grade = "B"
elif score >= 80:
    grade = "B-"
elif score >= 77:
    grade = "C+"
elif score >= 73:
    grade = "C"
elif score >= 70:
    grade = "C-"
elif score >= 67:
    grade = "D+"
if score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)                                        
    


    
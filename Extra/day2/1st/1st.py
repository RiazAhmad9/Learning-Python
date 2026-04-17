# Grading System


# Store float in 'score' variable
score = float(input("Enter the score: "))

# Stores a specific value in 'grade' variable considering the conditions
if score >= 93:
    grade = "A"
else:
    if score >= 90:
        grade = "A-"
    else:
        if score >= 87:
            grade = "B+"
        else:
            if score >= 83:
                grade = "B"
            else:
                if score >= 80:
                    grade = "B-"
                else:
                    if score >= 77:
                        grade = "C+"
                    else:
                        if score >= 73:
                            grade = "C"
                        else:
                            if score >= 70:
                                grade = "C-"
                            else:
                                if score >= 67:
                                    grade = "D+"
                                else:
                                    if score >= 60:
                                        grade = "D"
                                    else:
                                        grade = "F"

# Prints grade
print("Your grade is:", grade)                                        
    


    
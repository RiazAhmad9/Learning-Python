"""
grading_system
-----------------
Takes a score (0-100) and prints the corresponding letter grade.

- float(): allows decimal scores like 89.5
- while True + try/except: loops until valid input, catches non-numeric entries
- range check (0-100): blocks impossible scores
- if/elif/else chain: checks grades from highest to lowest — order matters,
  first matching condition wins and the rest are skipped
- grading(score): separate function keeps input logic and grading logic apart
- if __name__ == "__main__": ensures main() only runs when executed directly,
  not when imported as a module
"""

def main():
    while True:
        try:
            score = float(input("Score: "))
            if 0 <= score <= 100:
                break
            print("Enter between (1-100)")
        except ValueError:
            print("Please enter numbers only")
    grading(score)

def grading(score):
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
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
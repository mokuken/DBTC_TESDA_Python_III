student_grade = int(input("Input a numerical grade (0 to 100): "))

if student_grade <= 100:
    if student_grade == 100:
        print("Perfect Score")
    elif student_grade >= 90:
        print("Excellent Work")
    elif student_grade >=80:
        print("Great Job")
    elif student_grade >= 70:
        print("Good Effort")
    elif student_grade >= 60:
        print("Needs Improvement")
    else:
        print("Try Again")
else:
    print("Invalid Grade")

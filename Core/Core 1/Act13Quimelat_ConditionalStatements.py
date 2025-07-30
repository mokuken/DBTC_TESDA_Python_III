student_grade = int(input("Enter you grade: "))

if student_grade >= 90:
    print("Remark: Excellent")
elif student_grade > 80 and student_grade < 89:
    print("Remark: Very Good")
elif student_grade > 70 and student_grade < 79:
    print("Remark: Good")
elif student_grade > 60 and student_grade < 69:
    print("Remark: Passed")
else:
    print("Remark: Failed")

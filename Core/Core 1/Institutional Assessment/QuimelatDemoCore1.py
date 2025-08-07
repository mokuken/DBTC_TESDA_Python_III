# promp the user how many student to add with error handling
try:
    number_student = int(input("Enter number of students: "))
except ValueError:
    print("Invalid input, try again.")

# defined a function to compute the average of total grade
def compute_average(total_grade):
    return round(total_grade / 3, 2)

# Declared a list variable named students
students_list = []

# prompt and store the student name, average, remarks by looping based on number_student
for i in range(number_student):
    print("\nStudent", i+1, "Details:")
    name = input("Enter student name: ")

    try:
        # ask 3 grades with error handling
        grade1 = int(input("Enter grade 1: "))
        grade2 = int(input("Enter grade 2: "))
        grade3 = int(input("Enter grade 3: "))
    except ValueError:
        print("Invalid input, try again.")

    # sum all grades and store it in total_grade varaible
    total_grade = grade1 + grade2 + grade3

    # Use the total_grade as argument in compute_average() function to compute and return the average grade.
    average = compute_average(total_grade)

    # check if the average grade remarks passed or failed.
    if average >= 75:
        remarks = "Passed"
    else: 
        remarks = "Failed"

    # display the remark result
    print("Remark:", remarks)

    # store the name, average, and remarks to student_list as dictionary
    students_list.append({"student_name": name, "average": average, "remarks": remarks})


# Display the final output of student name, average, and remarks.
print("\n📋 Class Summary:")
for i in range(number_student):
    print(students_list[i]["student_name"], end = " - ")
    print("Average:", students_list[i]["average"], end = ", ")
    print("Remarks:", students_list[i]["remarks"])


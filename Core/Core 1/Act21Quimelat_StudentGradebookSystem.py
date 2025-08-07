# declared the names of the students in a list
student_names = ["Harly", "Ryan", "Jessie"]

# declared the subject with grades in tuple each student_names
grades_harly = (("Math", 85), ("English", 90))
grades_ryan = (("Math", 80), ("English", 85))
grades_jessie = (("Math", 90), ("English", 80))

# store the name, subject and grades in the dictionary
students = {
    student_names[0] : grades_harly,
    student_names[1] : grades_ryan,
    student_names[2] : grades_jessie
}

# loop each student in students dictionary
for name in students:
    print("\n" + name)
    grades = students[name]

    # calculate the average grade by adding the grades then divide how many subjects there are.
    total = 0
    count = 0
    for subject, grade in grades:
        print("-", subject, grade)
        total += grade
        count += 1

    average = total / count
    print("- Average:", average)
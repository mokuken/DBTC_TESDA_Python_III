employees = {}

# Ask the 3 employees of their name, earn per day, number of working days
for i in range(3):
    e_name = input("Enter employee name: ")
    daily_rate = int(input("Earn per day: "))
    working_days = int(input("Number of working days: "))

    # calculate the gross salary of the employee
    gross_salary = daily_rate * working_days

    # store the information in employees dictionary
    employees[e_name] = {"salary": gross_salary}

# Seperator
print("\nThe Tree Employees")

# print each employee name, gross salary and total salary combine of 3 employees
combine_salary = 0
for employee in employees:
    print(employee, "with a gross salary of", employees[employee]["salary"], "pesos.")
    combine_salary += employees[employee]["salary"]

print("\ntotal salary of all 3 employees combined:", combine_salary)

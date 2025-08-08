class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Course: {self.course}"

# Create student instances
student1 = Student("Ana", 18, "BSIT")
student2 = Student("Ben", 19, "BSA")
student3 = Student("Harly", 22, "BSCS")
student4 = Student("Jack", 20, "BSIT")
student5 = Student("Rolly", 19, "BSIT")
student6 = Student("Micheal", 22, "BSIT")
student7 = Student("Ryan", 18, "BSIT")
student8 = Student("Jessie", 19, "BSIT")
student9 = Student("Kenji", 21, "BSIT")
student10 = Student("Frenz", 20, "BSIT")

# Print student info
print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)
print(student7)
print(student8)
print(student9)
print(student10)

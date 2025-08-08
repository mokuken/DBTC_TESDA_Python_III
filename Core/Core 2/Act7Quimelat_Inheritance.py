# Task 1: Simple Inheritance

# Create a base class Person and a derived class Student.
class Person:
    # Create a constructor for the base class Person
    def __init__(self, name):
        self.name = name

    # Define a method introduce in the base class
    def introduce(self):
        print("Hi, I'm", self.name)

class Student(Person):
    def study(self):
        print(self.name, "is studying.")

# Create an instance of Student and call its methods.
student = Student("Ella")

# Call the methods from the Student class and its parent class
student.introduce()
student.study()


# Task 2: Problem Solving with Inheritanc

# # Create a base class Animal and two derived classes Dog and Cat.
class Animal:
    # Create a constructor for the base class Animal
    def __init__(self, name):
        self.name = name

    # Define a method make_sound in the base class
    def make_sound(self):
        pass

class Dog(Animal):
    # Override the make_sound method for Dog
    def make_sound(self):
        print("Woof! My name is", self.name)

class Cat(Animal):
    # Override the make_sound method for Cat
    def make_sound(self):
        print("Meow! My name is", self.name)

# Create instances of Dog and Cat, and call their make_sound methods.
dog = Dog("Browny")
cat = Cat("Kitty")

# Call the make_sound method for both instances
dog.make_sound()
cat.make_sound()
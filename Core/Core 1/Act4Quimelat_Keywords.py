# list of guest
guest_list = ["harly", "ryan", "jessie"]

# prompt user to input a name and age
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# find the name in the list and check if age is above 18
if name in guest_list:
    if age >= 18:
        print("Welcome,", name + "! You may enter.")
    else:
        print("Sorry", name, "you're too young to enter.")
else:
    print("Sorry, you're not on the list.")
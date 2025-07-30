# declared the number and special character to string value
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
special_char = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
                '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
                '_', '`', '{', '|', '}', '~']

# promp the user for a password
password = input("Enter a password: ")
pass_stegnth = 0

if len(password) >= 8:
    pass_stegnth += 1

# check the password if it contains numbers
for number in numbers:
    if number in password:
        pass_stegnth += 1
        break

# check the password if it contains special character
for char in special_char:
    if char in password:
        pass_stegnth += 1
        break

# check the password if it contains uppercase
for char in password:
    if char >= 'A' and char <= 'Z':
        pass_stegnth += 1
        break

# check the password if it contains lowercase
for char in password:
    if char >= 'a' and char <= 'z':
        pass_stegnth += 1
        break

# evaluate the strength of the password
if pass_stegnth == 2:
    print("The password is weak")
elif pass_stegnth == 3:
    print("The password is medium")
elif pass_stegnth == 5:
    print("The password is strong")
else:
    print("The password is too weak")
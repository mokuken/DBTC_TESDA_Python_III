# Activity A
print('\033[95m\nActivity A: While Loop - "Number Counter"\033[0m')
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    print(i)


# Activity B
print('\033[92m\nActivity B: While Loop - "Password Retry"\033[0m')
while True:
    password = input("Enter password: ")
    if password == "admin123":
        print("Access granted!")
        break
    else:
        print("Access denied!")


# Acrivity C
print('\033[93m\nActivity C: For Loop - "Multiplication Table"\033[0m')
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Activity D
print('\033[94m\nActivity D: For Loop - "Name Repeater"\033[0m')
name = input("Enter your name: ")
repeat_name = int(input("How many times to display your name?: "))

for i in range(repeat_name):
    print(name)


# Activity E
print('\033[96m\nActivity E: For Loop - "List Summer"\033[0m')
numbers = []
sum = 0

while True:
    add_num = input("Enter a number, type (stop) to exit: ")

    if add_num != "stop":
        numbers.append(int(add_num))
    else:
        break

for number in numbers:
    sum += number

print("Numbers:", numbers)
print("Sum:", sum)

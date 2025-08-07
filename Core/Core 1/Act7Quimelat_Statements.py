# declare the basic pay and deduction variables with value
basic_pay = 1000
deduction = 480

# calculate the net pay by deducting the basic pay
net_pay = basic_pay - deduction


# print the net pay and if its sufficient or else too low
print("Net Pay:", net_pay)
if net_pay >= 500:
    print("Net pay is sufficient")
else:
    print("Net pay too low")


# declared a net_pay variable with a fixed value
net_pay = 500

# added a fixed bonus using assignment operator
net_pay += 100

# check if its above 500 and even
if net_pay > 500 and net_pay % 2 == 0 :
    print("Final pay is above 500 and even:", net_pay)
else:
    print("Final pay does not meet the conditions.")

# print net_pay 3 times using for loop
for i in range(3):
    print(net_pay)
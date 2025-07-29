# ask the user for the trip expense information
budget = int(input("Enter Total trip budget (₱): "))
transportation = int(input("Enter estimated transportation cost (₱): "))
food = int(input("Enter estimated food cost (₱): "))
activity = int(input("Enter estimated activity cost (₱): "))

# calculate the total cost
total_cost = transportation + food + activity

# deduct the total cost to the budget
difference = budget - total_cost

# and check if the total cost is within the budget
if total_cost < budget:
    print("You are within your budget. You still have ₱" + str(difference), "left. Enjoy your trip!")
elif total_cost > budget:
    print("You are over budget by ₱" + str(-difference) + ". Consider adjusting your plan.")
else:
    print("You spent your entire budget. Plan executed perfectly!")
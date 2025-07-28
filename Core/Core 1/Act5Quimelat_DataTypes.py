# ask the user name and budget
name = input("Enter your name: ")
budget = float(input("Enter your budget: "))

categories = ("Fruits", "Vegetables", "Dairy", "Snacks")

# ask the user how many items to buy
numberOfItems = int(input("How many items you want to buy?: "))

grocery_list = []

# enter the item name
for i in range(numberOfItems):
    grocery_list.append(input("Enter the item name: "))

# convert the grocery_list to tuple to prevent duplicates
set_grocery_list = set(grocery_list)


items = {}
total_price = 0


# set the category and price of each inputed item
for item in set_grocery_list:
    print("\nFor", item, "item")

    # Keep asking for category until it's valid
    while True:
        item_category = input("Enter the item category: ")
        if item_category in categories:
            break
        else:
            print("Category does not exist. Please try again.")

    # Once valid, proceed
    item_price = float(input("Enter the item price: "))
    total_price += item_price
    items[item] = {"category": item_category, "price": item_price}

# calculate the total remaining budget
remaining_budget = budget - total_price

if total_price <= budget:
    budget_status = "Within Budget"
else:
    budget_status = "Over the budget"


# Output summary
print("\nname of the shopper:", name)
print("number of items:", numberOfItems)
print("unique items:", len(set_grocery_list))
print("total cost:", total_price)
print("Budget status:", budget_status)

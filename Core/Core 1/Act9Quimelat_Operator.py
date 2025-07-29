# Initialize an empty dictionary to store grocery inventory
grocery_inventory = {}

# Start an infinite loop for the menu-driven program
while True:
    # Display menu options
    print("\n1. Add Item")
    print("2. Increase Stock")
    print("3. Decrease Stock")
    print("4. View Inventory")
    print("5. Exit")

    # Get user's choice
    user_choice = int(input("Choose an option: "))

    # Option 1: Add a new item to the inventory
    if user_choice == 1:
        item_name = input("Enter item name: ")
        # Check if item does not exist
        if item_name not in grocery_inventory:
            initial_stock = int(input("Enter initial stock: "))
            grocery_inventory[item_name] = initial_stock
            print("Item added.")
        else:
            print("Item already exists.")

    # Option 2: Increase stock of an existing item
    elif user_choice == 2:
        item_name = input("Enter item name: ")
        # Check if item exists
        if item_name in grocery_inventory:
            add_quantity = int(input("Enter quantity to add: "))
            grocery_inventory[item_name] += add_quantity
            print("Stock increased.")
        else:
            print("Item not found.")

    # Option 3: Decrease stock of an existing item
    elif user_choice == 3:
        item_name = input("Enter item name: ")
        # Check if item exists
        if item_name in grocery_inventory:
            remove_quantity = int(input("Enter quantity to remove: "))
            # Ensure enough stock is available
            if remove_quantity <= grocery_inventory[item_name]:
                grocery_inventory[item_name] -= remove_quantity
                print("Stock decreased.")
            else:
                print("Not enough stock.")
        else:
            print("Item not found.")

    # Option 4: View current inventory
    elif user_choice == 4:
        print("\nCurrent Inventory:")
        for item_name, stock_count in grocery_inventory.items():
            print("-", item_name + ":", stock_count)

    # Option 5: Exit the program
    elif user_choice == 5:
        print("Exiting Grocery Store Inventory Manager.")
        break

    # Handle invalid menu options
    else:
        print("Invalid option. Please choose between 1 and 5.")

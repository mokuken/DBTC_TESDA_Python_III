menu = {
    "casava": 15,
    "pansit tinapay": 25,
    "turon": 12,
    "banana q": 20,
    "puto": 10
}

basket = {}
total_price = 0

is_manang_here = input("Is Manang here? (yes/no): ")

if is_manang_here == "yes":
    print("Ara na si Manang Ma'am! break time na!")

    print("\nAmo ni ang mga paninda ni Manang:")
    for food, price in menu.items():
        print("-", food, "-", "₱" + str(price))
    
    
    selected = input("\nAno pa baklon mo? (type 'wala na' kon tapos ka): ")
    while True: 
        if selected == "wala na":
            break
        else:
            pieces = int(input("Pila ka '" + selected + "'?: "))
            if selected in menu:
                basket[selected] = pieces
            selected = input("Ano pa? (type 'wala na' kon tapos ka): ")

    print("\nMuni tanan imo ginbakal ha:")
    for food, pieces in basket.items():
        print("-", str(pieces), "x" , food)
        total_price += pieces * menu[food]
    
    print("\nPila tanan?: ₱" + str(total_price))

    budget = int(input("\nPila pa Kwarta mo?: ₱"))

    print("Imo sinsilyo ₱" + str(budget - total_price), "Salamat!")
else:
    print("No break time yet. Wala pa si Manang.")


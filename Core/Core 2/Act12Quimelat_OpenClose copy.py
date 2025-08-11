customer_discount = {
    "regular": 0.05,  # 5% discount for regular customers
    "vip": 0.15,  # 15% discount for VIP customers
}

def get_access(customer_type, total_amount):
    return total_amount * customer_discount.get(customer_type, 0)  # Default to 0 if role not found

customer_discount["senior citizen"] = 0.20
customer_discount["employee"] = 0.10

for type in customer_discount:
    print(type, "Discount",get_access(type, 1000))

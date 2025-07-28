# tuple of school supplies
schoolSupplies = ("notebook", "pen", "eraser")

# print supplies once
print(schoolSupplies)

# print each supply by index
print(schoolSupplies[0])
print(schoolSupplies[1])
print(schoolSupplies[2])

# check if the pen is in the school supplies
if "pen" in schoolSupplies:
    print("Yes, pen is in the tuples!")


# challenge
c = list(schoolSupplies)
c[1] = "ballpen"
schoolSupplies = tuple(c)
print(schoolSupplies)

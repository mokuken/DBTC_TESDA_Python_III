time_capsule = ("letter to future self", "photos", "USB drive")

# Try to replace "photos" with "video recording".
try:
    time_capsule[1] = "video recording"
except TypeError as e:
    print(e, "\n")

# Attempt to remove "USB drive"
try:
    time_capsule.remove("USB drive")
except AttributeError as e:
    print(e, "\n")

# Add "newspaper" to the end
try:
    time_capsule.append("newspaper")
except AttributeError as e:
    print(e, "\n")

# Read and review "letter to future self"
print(time_capsule[0], "\n")

# Attempt to reorder the items
ordered_time_capsule = (time_capsule[2], time_capsule[0], time_capsule[1])

print("Final Tuple")
print("1.", ordered_time_capsule[0])
print("2.", ordered_time_capsule[1])
print("3.", ordered_time_capsule[2])

# Reflection Questions
# 1. Which actions were rejected, and why?
# Answer: replacing and removing methods/functions are the actions were rejected becasue tuple
# is immutable it means once its created it cannot be change, add, remove the elements

# 2. How is immutability useful in this case?
# Answer: Its is very use when it come to a scenario were you put a data that should not be changable
# like person's gender, name, blood type.
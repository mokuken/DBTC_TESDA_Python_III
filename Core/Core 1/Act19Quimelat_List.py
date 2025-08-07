task_list = ["wake up", "brush teeth", "eat breakfast"]

task_list[1] = "take a shower"

task_list.append("exercise")

task_list.remove("wake up")

task_list.insert(0, "journal")

task_list.append("check messages")

print("1.", task_list[0])
print("2.", task_list[1])
print("3.", task_list[2])
print("4.", task_list[3])
print("5.", task_list[4])


# Reflection questions
# 1. What operations did you perform in this task?
# Answer: I performed append, remove, insert, and replace an element using the index

# 2 Could you perform the same steps if this were a tuple? Why or why not?
# Answer: No, its becasue tuple is an immutable data type you cant add, remove, 
# or insert once the tuple is created
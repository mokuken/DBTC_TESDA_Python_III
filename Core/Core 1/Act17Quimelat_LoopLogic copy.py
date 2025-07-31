# Part 1
for number in range(1, 50):
    if number % 2 == 0:
        print(number, end = " ")

print()
# Part 2
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        continue
    if number % 2 == 0:
        print(number, end = " ")

print()
# Part 3
number = 0
sum_odd_number = 0
while number <= 100:
    if number % 2 != 0:
        sum_odd_number += number
        if sum_odd_number >=  1000:
            print("The number", number, "that exceed 1000")
            break
    number += 1

print(sum_odd_number)

# Part 4
number = [1, 2, 3, 4, 5]
for i in number:
    for j in number:
        print("%3d" % (i * j), end=" ")
    print()


# Part 5
# for vs while:
# - for: best for known iteration counts, concise and clear.
# - while: better for condition-based loops, but can risk infinite loops if not careful.
#
# break vs continue:
# - break: exits loop immediately, useful to stop early.
# - continue: skips current iteration, useful to ignore certain cases.
# Both control flow but can hurt readability if overused.
#
# Nested loops for formatting:
# - outer loop = rows, inner loop = columns.
# - intuitive for tables/matrices, but can get complex if deeply nested.
# - fine for small data, but nested loops mean higher time complexity.
#
# Overall:
# for loops + simple nested loops are most readable/efficient for fixed iteration tasks.
# break/continue help control flow but should be used sparingly.

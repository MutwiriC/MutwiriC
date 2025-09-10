"""
syntax:
outer loop:
        inner loop:
                statements of inner loop
        statements of outer loop

"""

"""
types of nested loops:

for loop:
        for loop:
                statement of inner for loop
        statement of for loop
-----
while loop:
        while loop:
                statement of inner while loop
        statement of while loop
---
while loop:
        for loop:
                statement of inner for loop
        statement of while loop
----
for loop:
        while loop:
                statement of inner while loop
        statement of for loop
"""

"""
they are used in nested list, Arrays, or matrix

"""

list_fruits = ["Mango", "Apple", "Grapes", "Banana"]
for fruit in list_fruits:
    for i in fruit:
        print(i, end="@")
    print()


color = ["red", "green", "blue"]
items = ["apple", "veggies", "shirt"]

for x in color:
    for y in items:
        print(x, y)


# print right triangle
for i in range(11):
    for j in range(i):
        print("*", end=" ")
    print(" ")

# using while loop
i = 11
while i > 0:
    j = 11
    while j > i:
        print("*", end=" ")
        j = j - 1
    i = i - 1
    print()

# how to append 2 lists
list1 = [10, 25, 30]
list2 = [60, 15, 50]
result = []
for i in list1:
    for j in list2:
        result.append(i + j)
print(result)

# multiplying two lists
list1 = [2, 4, 6]
list2 = [2, 4, 6]
for i in list1:
    for j in list2:
        if i == j:
            continue
        print(i, "*", j, "=", i * j)

# finding perfect numbers
a = 1
while a <= 100:
    y_sum = 0

    for i in range(1, a):
        if a % i == 0:
            y_sum = y_sum + i
    if y_sum == a:
        print("Perfect number: ", a)
    a = a + 1
print("Done checking up to 100")

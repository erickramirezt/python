# PYTHON - JOIN LISTS

# JOIN TWO LISTS
# THERE ARE SEVERAL WAYS TO JOIN, OR CONCATENATE, TWO OR MORE LISTS IN PYTHON.
# ONE OF THE EASIEST WAYS ARE BY USING THE + OPERATOR.
# JOIN TWO LIST:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# ANOTHER WAY TO JOIN TWO LISTS ARE BY APPENDING ALL THE ITEMS FROM LIST2 INTO LIST1, ONE BY ONE:
# APPEND LIST2 INTO LIST1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)

print(list1)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]

# OR YOU CAN USE THE EXTEND() METHOD, WHICH PURPOSE IS TO ADD ELEMENTS FROM ONE LIST TO ANOTHER LIST:
# USE THE EXTEND() METHOD TO ADD LIST2 AT THE END OF LIST1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # OUTPUT: ['a', 'b', 'c', 1, 2, 3]
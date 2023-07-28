# PYTHON - ACCESS TUPLE ITEMS

# ACCESS TUPLE ITEMS
# YOU CAN ACCESS TUPLE ITEMS BY REFERRING TO THE INDEX NUMBER, INSIDE SQUARE BRACKETS:
# PRINT THE SECOND ITEM IN THE TUPLE:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  # OUTPUT: banana
# NOTE: THE FIRST ITEM HAS INDEX 0.

# NEGATIVE INDEXING
# NEGATIVE INDEXING MEANS BEGINNING FROM THE END 
# -1 REFERS TO THE LAST ITEM, -2 REFERS TO THE SECOND LAST ITEM ETC.
# PRINT THE LAST ITEM OF THE TUPLE:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # OUTPUT: cherry

# RANGE OF INDEXES
# YOU CAN SPECIFY A RANGE OF INDEXES BY SPECIFYING WHERE TO START AND WHERE TO END THE RANGE.
# WHEN SPECIFYING A RANGE, THE RETURNED TUPLE WILL CONTAIN THE SPECIFIED ITEMS,
# RETURN THE THIRD, FOURTH, AND FIFTH ITEM:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # OUTPUT: ('cherry', 'orange', 'kiwi')
# NOTE: THE SEARCH WILL START AT INDEX 2 (INCLUDED) AND END AT INDEX 5 (NOT INCLUDED).
# REMEMBER THAT THE FIRST ITEM HAS INDEX 0.

# BY LEAVING OUT THE START VALUE, THE RANGE WILL START AT THE FIRST ITEM:
# THIS EXAMPLE RETURNS THE ITEMS FROM THE BEGINNING TO "ORANGE":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])  # OUTPUT: ('apple', 'banana', 'cherry', 'orange')

# BY LEAVING OUT THE END VALUE, THE RANGE WILL GO ON TO THE END OF THE LIST:
# THIS EXAMPLE RETURNS THE ITEMS FROM "CHERRY" AND TO THE END:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])  # OUTPUT: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# RANGE OF NEGATIVE INDEXES
# SPECIFY NEGATIVE INDEXES IF YOU WANT TO START THE SEARCH FROM THE END OF THE TUPLE:
# THIS EXAMPLE RETURNS THE ITEMS FROM INDEX -4 (INCLUDED) TO INDEX -1 (EXCLUDED)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # OUTPUT: ('orange', 'kiwi', 'melon')

# CHECK IF ITEM EXISTS
# TO DETERMINE IF A SPECIFIED ITEM IS PRESENT IN A TUPLE USE THE IN KEYWORD:
# CHECK IF "APPLE" IS PRESENT IN THE TUPLE:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")  # OUTPUT: Yes, 'apple' is in the fruits tuple
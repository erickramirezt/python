# PYTHON LISTS
mylist = ["apple", "banana", "cherry"]

# LIST
# LISTS ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE.
""" LISTS ARE ONE OF 4 BUILT-IN DATA TYPES IN PYTHON USED TO STORE COLLECTIONS OF DATA, THE OTHER 3 ARE TUPLE,
SET AND DICTIONARY, ALL WITH DIFFERENT QUALITIES AND USAGE. """
# LISTS ARE CREATED USING SQUARE BRACKETS:
# EXAMPLE
thislist = ["apple", "banana", "cherry"]
print(thislist)

# LIST ITEMS
# LIST ITEMS ARE ORDERED, CHANGEABLE, AND ALLOW DUPLICATE VALUES.
# LIST ITEMS ARE INDEXED, THE FIRST ITEM HAS INDEX [0], THE SECOND ITEM HAS INDEX [1] ETC.

# ORDERED
# WHEN WE SAY THAT LISTS ARE ORDERED, IT MEANS THAT THE ITEMS HAVE A DEFINED ORDER, AND THAT ORDER WILL NOT CHANGE.
# IF YOU ADD NEW ITEMS TO A LIST, THE NEW ITEMS WILL BE PLACED AT THE END OF THE LIST.
# NOTE: THERE ARE SOME LIST METHODS THAT WILL CHANGE THE ORDER, BUT IN GENERAL: THE ORDER OF THE ITEMS WILL NOT CHANGE.

# CHANGEABLE
# THE LIST IS CHANGEABLE, MEANING THAT WE CAN CHANGE, ADD, AND REMOVE ITEMS IN A LIST AFTER IT HAS BEEN CREATED.

# ALLOW DUPLICATES
# SINCE LISTS ARE INDEXED, LISTS CAN HAVE ITEMS WITH THE SAME VALUE:
# EXAMPLE
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# LIST LENGTH
# TO DETERMINE HOW MANY ITEMS A LIST HAS, USE THE len() FUNCTION:
# EXAMPLE
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# LIST ITEMS - DATA TYPES
# LIST ITEMS CAN BE OF ANY DATA TYPE:
# EXAMPLE
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A LIST CAN CONTAIN DIFFERENT DATA TYPES:
# EXAMPLE
list1 = ["abc", 34, True, 40, "male"]

# TYPE()
# FROM PYTHON'S PERSPECTIVE, LISTS ARE DEFINED AS OBJECTS WITH THE DATA TYPE 'list':
# EXAMPLE
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# THE list() CONSTRUCTOR
# IT IS ALSO POSSIBLE TO USE THE list() CONSTRUCTOR WHEN CREATING A NEW LIST.
# EXAMPLE
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)

# PYTHON COLLECTIONS (ARRAYS)
# THERE ARE FOUR COLLECTION DATA TYPES IN THE PYTHON PROGRAMMING LANGUAGE:
# LIST IS A COLLECTION WHICH IS ORDERED AND CHANGEABLE. ALLOWS DUPLICATE MEMBERS.
# TUPLE IS A COLLECTION WHICH IS ORDERED AND UNCHANGEABLE. ALLOWS DUPLICATE MEMBERS.
# SET IS A COLLECTION WHICH IS UNORDERED AND UNINDEXED. NO DUPLICATE MEMBERS.
# DICTIONARY IS A COLLECTION WHICH IS UNORDERED, CHANGEABLE AND INDEXED. NO DUPLICATE MEMBERS.
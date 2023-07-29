# PYTHON SETS
myset = {"apple", "banana", "cherry"}

# SET
# SETS ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE
# SET IS ONE OF 4 BUILT-IN DATA TYPES IN PYTHON USED TO STORE COLLECTIONS OF DATA, THE 
# OTHER 3 ARE LIST, TUPLE, AND DICTIONARY, ALL WITH DIFFERENT QUALITIES AND USAGE
# A SET IS A COLLECTION WHICH IS UNORDERED, UNCHANGEABLE, AND UNINDEXED
# NOTE: SET ITEMS ARE UNCHANGEABLE, BUT YOU CAN REMOVE ITEMS AND ADD NEW ITEMS

# SETS ARE WRITTEN WITH CURLY BRACKETS
# EXAMPLE
# CREATE A SET
thisset = {"apple", "banana", "cherry"}
print(thisset)
# NOTE: SET ARE UNORDERED, SO YOU CANNOT BE SURE IN WHICH ORDER THE ITEMS WILL APPEAR

# SET ITEMS
# SET ITEMS ARE UNORDERED, UNCHANGEABLE, AND DO NOT ALLOW DUPLICATE VALUES

# UNORDERED
# UNORDERED MEANS THAT THE ITEMS IN A SET DO NOT HAVE A DEFINED ORDER
# SET ITEMS CAN APPEAR IN A DIFFERENT ORDER EVERY TIME YOU USE THEM, AND CANNOT BE
# REFERRED TO BY INDEX OR KEY

# UNCHANGEABLE
# SET ITEMS ARE UNCHANGEABLE, MEANING THAT WE CANNOT CHANGE THE ITEM AFTER THE SET HAS 
# BEEN CREATED
# ONCE A SET IS CREATED, YOU CANNOT CHANGE ITS ITEMS, BUT YOU CAN ADD NEW ITEMS AND ADD 
# NEW ITEMS

# DUPLICATE NOT ALLOWED
# SETS CANNOT HAVE TWO ITEMS WITH THE SAME VALUE
# EXAMPLE
# DUPLICATE VALUES WILL BE IGNORED
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# NOTE: THE VALUES TRUE AND 1 ARE THE SAME VALUE IN SETS, AND ARE TREATED AS DUPLICATES
# EXAMPLE
# TRUE AND 1 IS CONSIDERED THE SAME VALUE
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# GET THE LENGTH OF A SET
# TO DETERMINE HOW MANY ITEMS A SET HAS, USE THE len() METHOD
# EXAMPLE
# GET THE NUMBER OF ITEMS IN A SET
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# SET ITEMS - DATA TYPES
# SET ITEMS CAN BE OF ANY DATA TYPE
# EXAMPLE
# STRING, INTEGER AND BOOLEAN DATA TYPES
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, False}

# A SET CAN CONTAIN DIFFERENT DATA TYPES
# EXAMPLE
# A SET WITH STRINGS, INTEGER AND BOOLEAN VALUES
set1 = {"abc", 34, True, 40, "male"}

# TYPE
# FROM PYTHON'S PERSPECTIVE, SETS ARE DEFINED AS OBJECTS WITH THE DATA TYPE 'set'
# <class 'set'>
# EXAMPLE
# WHAT IS THE DATA TYPE OF A SET?
myset = {"apple", "banana", "cherry"}
print(type(myset))

# THE SET() CONSTRUCTOR
# IT IS ALSO POSSIBLE TO USE THE set() CONSTRUCTOR TO MAKE A SET
# EXAMPLE
# USING THE set() CONSTRUCTOR TO MAKE A SET
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


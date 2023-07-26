# PYTHON - ADD LIST ITEMS

# APPEND ITEMS
# TO ADD AN ITEM TO THE END OF THE LIST, USE THE APPEND() METHOD:
# EXAMPLE
# USING THE APPEND() METHOD TO APPEND AN ITEM:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# INSERT ITEMS
# TO INSERT A LIST ITEM AT A SPECIFIC INDEX, USE THE INSERT() METHOD.
# THE INSERT() METHOD INSERTS AN ITEM AT THE SPECIFIED INDEX:
# EXAMPLE
# INSERT AN ITEM AS THE SECOND POSITION:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# NOTE: AS A RESULT OF THE EXAMPLE ABOVE, THE LIST WILL NOW CONTAIN 4 ITEMS.

# EXTEND LIST
# TO INSERT ELEMENTS FROM ONE LIST TO ANOTHER LIST, USE THE EXTEND() METHOD.
# EXAMPLE
# ADD THE ELEMENTS OF TROPICAL TO THISLIST:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# THE ELEMENTS WILL BE ADDED TO THE END OF THE LIST.

# ADD ANY ITERABLE
""" THE EXTEND() METHOD DOES NOT HAVE TO APPEND LISTS, YOU CAN ADD ANY ITERABLE OBJECT (TUPLE, SET, DICTIONARY 
ETC.). """
# EXAMPLE
# ADD ELEMENTS OF A TUPLE TO A LIST:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
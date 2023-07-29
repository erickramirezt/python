# PYTHON - ADD SET ITEMS

# ADD ITEMS
# ONCE A SET IS CREATED, YOU CANNOT CHANGE ITS ITEMS, BUT YOU CAN ADD NEW ITEMS
# TO ADD ONE ITEM TO A SET USE THE add() METHOD
# EXAMPLE
# ADD AN ITEM TO A SET, USING THE add() METHOD
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# ADD SETS
# TO ADD ITEMS FROM ANOTHER SET INTO THE CURRENT SET, USE THE update() METHOD
# EXAMPLE
# ADD ELEMENTS FROM tropical INTO thisset
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# ADD ANY ITERABLE
# THE OBJECT IN THE update() METHOD DOES NOT HAVE TO BE A SET, IT CAN BE ANY ITERABLE
# OBJECT (TUPLE, LISTS, DICTIONARIES ETC.)
# EXAMPLE
# ADD ELEMENTS OF A LIST TO AT SET
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

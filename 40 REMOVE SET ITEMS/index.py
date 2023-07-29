# PYTHON - REMOVE SET ITEMS

# REMOVE ITEM
# TO REMOVE AN ITEM IN A SET, USE THE remove(), or the discard() METHOD
# EXAMPLE
# REMOVE "banana" BY USING THE remove() METHOD
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# NOTE: IF THE ITEM TO REMOVE DOES NOT EXIST, remove() WILL RAISE AN ERROR

# EXAMPLE
# REMOVE "banana" BY USING THE discard() METHOD
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# NOTE: IF THE ITEM TO REMOVE DOES NOT EXIST, discard() WILL NOT RAISE AN ERROR

# YOU CAN ALSO USE THE pop(), METHOD TO REMOVE AN ITEM, BUT THIS METHOD WILL REMOVE A
# RANDOM ITEM, SO YOU CANNOT BE SURE WHAT ITEM THAT GETS REMOVED
# THE RETURN VALUE OF THE pop() METHOD IS THE REMOVED ITEM
# EXAMPLE
# REMOVE THE LAST ITEM BY USING THE pop() METHOD
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# NOTE: SETS ARE UNORDERED, SO WHEN USING THE pop() METHOD, YOU WILL NOT KNOW WHICH ITEM
# THAT GETS REMOVED

# EXAMPLE
# THE clear() METHOD EMPTIES THE SET
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# EXAMPLE
# THE del KEYWORD WILL DELETE THE SET COMPLETELY
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
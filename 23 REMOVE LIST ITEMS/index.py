# PYTHON - REMOVE LIST ITEMS

# REMOVE SPECIFIED ITEM
# THE REMOVE() METHOD REMOVES THE SPECIFIED ITEM.
# EXAMPLE
# REMOVE "BANANA":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# REMOVE SPECIFIED INDEX
# THE POP() METHOD REMOVES THE SPECIFIED INDEX.
# EXAMPLE
# REMOVE THE SECOND ITEM:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# IF YOU DO NOT SPECIFY THE INDEX, THE POP() METHOD REMOVES THE LAST ITEM.
# EXAMPLE
# REMOVE THE LAST ITEM:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# THE DEL KEYWORD ALSO REMOVES THE SPECIFIED INDEX:
# EXAMPLE
# REMOVE THE FIRST ITEM:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# THE DEL KEYWORD CAN ALSO DELETE THE LIST COMPLETELY.

# EXAMPLE
# DELETE THE ENTIRE LIST:
thislist = ["apple", "banana", "cherry"]
del thislist

# CLEAR THE LIST
# THE CLEAR() METHOD EMPTIES THE LIST.
# THE LIST STILL REMAINS, BUT IT HAS NO CONTENTS.
# EXAMPLE
# CLEAR THE LIST CONTENTS:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# PYTHON - REMOVE DICTIONARY ITEMS

# REMOVING ITEMS
# THERE ARE SEVERAL METHODS TO REMOVE ITEMS FROM A DICTIONARY
# EXAMPLE
# THE pop() METHOD REMOVES THE ITEM WITH THE SPECIFIED KEY NAME
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# EXAMPLE
# THE del KEYWORD REMOVES THE ITEM WITH THE SPECIFIED KEY NAME
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# EXAMPLE
# THE del KEYWORD CAN ALSO DELETE THE DICTIONARY COMPLETELY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
print(thisdict)

# EXAMPLE
# THE clear() METHOD EMPTIES THE DICTIONARY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)
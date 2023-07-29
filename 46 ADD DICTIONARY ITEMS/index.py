# PYTHON - ADD DICTIONARY ITEMS

# ADDING ITEMS
# ADDING AN ITEM TO THE DICTIONARY IS DONE BY USING A NEW INDEX KEY AND ASSIGNING A VALUE 
# TO IT
# EXAMPLE
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# UPDATE DICTIONARY
# THE update() METHOD WILL UPDATE THE DICTIONARY WITH THE ITEMS FROM THE GIVEN ARGUMENT
# IF THE ITEM DOES NOT EXIST, THE ITEM WILL BE ADDED
# THE ARGUMENT MUST BE A DICTIONARY, OR AN ITERABLE OBJECT WITH KEY:VALUE PAIRS
# EXAMPLE
# ADD A COLOR ITEM TO THE DICTIONARY BY USING THE update() METHOD
# EXAMPLE
# ADD A COLOR ITEM TO THE DICTIONARY BY USING THE update() METHOD
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
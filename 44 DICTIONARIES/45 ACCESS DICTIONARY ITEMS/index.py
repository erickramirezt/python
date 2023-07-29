# PYTHON - ACCESS DICIONARY ITEMS

# ACCESSING ITEMS
# YOU CAN ACCESS THE ITEMS OF A DICTIONARY BY REFERRING TO ITS KEY NAME, INSIDE SQUARE
# BRACKETS
# EXAMPLE
# GET THE VALUE OF THE "model" KEY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# THERE IS ALSO A METHOD CALLED get() THAT WILL GIVE YOU THE SAME RESULT
# EXAMPLE
# GET THE VALUE OF THE "model" KEY
x = thisdict.get("model")

# GET KEYS
# THE keys() METHOD WILL RETURN A LIST OF ALL THE KEYS IN THE DICTIONARY
# EXAMPLE
# GET A LIST OF THE KEYS
x = thisdict.keys()

# THE LIST OF THE KEYS IS A VIEW OF THE DICTIONARY, MEANING THAT ANY CHANGES DONE TO THE
# DICTIONARY WILL BE REFLECTED IN THE KEYS LIST
# EXAMPLE
# ADD A NEW ITEM TO THE ORIGINAL DICTIONARY, AND SEE THAT THE KEYS LIST GETS UPDATED AS
# WELL
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
car["color"] = "white"
print(x)

# GET VALUES
# THE values() METHOD WILL RETURN A LIST OF ALL THE VALUES IN THE DICTIONARY
# EXAMPLE
# GET A LIST OF THE VALUES
x = thisdict.values()

# THE LIST OF THE VALUES IS A VIEW OF THE DICTIONARY, MEANING THAT ANY CHANGES DONE TO THE
# DICTIONARY WILL BE REFLECTED IN THE VALUES LIST
# EXAMPLE
# MAKE A CHANGE IN THE ORIGINAL DICTIONARY, AND SEE THAT THE VALUES LIST GETS UPDATED AS
# WELL
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)

# EXAMPLE
# ADD A NEW ITEM TO THE ORIGINAL DICTIONARY, AND SEE THAT THE VALUES LIST GETS UPDATED AS
# WELL
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)
car["color"] = "red"
print(x)

# GET ITEMS
# THE items() METHOD WILL RETURN EACH ITEM IN A DICTIONARY, AS TUPLES IN A LIST
# EXAMPLE
# GET A LIST OF THE KEY:VALUE PAIRS
x = thisdict.items()
# THE RETURNED LIST IS A VIEW OF THE ITEMS OF THE DICTIONARY, MEANING THAT ANY CHANGES 
# DONE TO THE DICTIONARY WILL BE REFLECTED IN THE ITEMS LIST
# EXAMPLE
# MAKE A CHANGE IN THE ORIGINAL DICTIONARY, AND SEE THAT THE ITEMS LIST GETS UPDATED AS
# WELL
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

# EXAMPLE
# ADD A NEW ITEM TO THE ORIGINAL DICTIONARY, AND SEE THAT THE ITEMS LIST GETS UPDATED AS
# WELL
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["color"] = "red"
print(x)

# CHECK IF KEY EXISTS
# TO DETERMINE IF A SPECIFIED KEY IS PRESENT IN A DICTIONARY USE THE in KEYWORD
# EXAMPLE
# CHECK IF "model" IS PRESENT IN THE DICTIONARY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# PYTHON - COPY DICTIONARIES

# COPY A DICTIONARY
# YOU CANNOT COPY A DICTIONARY SIMPLY BY TYPING dict2 = dict1, BECAUSE: dict2 WILL ONLY
# BE A REFERENCE TO dict1, AND CHANGES MADE IN dict1 WILL AUTOMATICALLY ALSO BE MADE IN
# dict2
# THERE ARE WAYS TO MAKE A COPY, ONE WAY IS TO USE THE built-in Dictionary method copy()

# EXAMPLE
# MAKE A COPY OF A DICTIONARY WITH THE copy() METHOD
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# ANOTHER WAY TO MAKE A COPY IS TO USE THE built-in method dict()

# EXAMPLE
# MAKE A COPY OF A DICTIONARY WITH THE dict() METHOD
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# PYTHON - CHANGE DICTIONARY ITEMS

# CHANGE VALUES
# YOU CAN CHANGE THE VALUE OF A SPECIFIC ITEM BY REFERRING TO ITS KEY NAME
# EXAMPLE
# CHANGE THE "year" TO 2018
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# UPDATE DICTIONARY
# THE update() METHOD WILL UPDATE THE DICTIONARY WITH THE ITEMS FROM THE GIVEN ARGUMENT
# THE ARGUMENT MUST BE A DICTIONARY, OR AN ITERABLE OBJECT WITH KEY:VALUE PAIRS
# EXAMPLE
# UPDATE THE "year" OF THE CAR BY USING THE update() METHOD
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})


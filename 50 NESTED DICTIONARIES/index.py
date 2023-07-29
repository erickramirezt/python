# PYTHON - NESTED DICTIONARIES

# NESTED DICTIONARIES
# A DICTIONARY CAN CONTAIN DICTIONARIES, THIS IS CALLED NESTED DICTIONARIES

# EXAMPLE
# CREATE A DICTIONARY THAT CONTAINS THREE DICTIONARIES
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# OR, IF YOU WANT TO ADD THREE DICTIONARIES INTO A NEW DICTIONARY

# EXAMPLE
# CREATE THREE DICTIONARIES, THEN CREATE ONE DICTIONARY THAT WILL CONTAIN THE OTHER THREE
# DICTIONARIES
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# ACCESSING ITEMS IN A NESTED DICTIONARY
# TO ACCESS ITEMS FROM A NESTED DICTIONARY, YOU USE THE NAME OF THE DICTIONARIES, 
# STARTING WITH THE OUTER DICIONARY

# EXAMPLE
# PRINT THE NAME OF CHILD 2
print(myfamily["child2"]["name"])
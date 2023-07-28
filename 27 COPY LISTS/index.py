# PYTHON - COPY LISTS

# COPY A LIST
""" YOU CANNOT COPY A LIST SIMPLY BY A TYPING LIST2 = LIST1, BECAUSE: LIST2 WILL ONLY BE A REFERENCE TO LIST1, 
AND CHANGES MADE IN LIST1 WILL AUTOMATICALLY ALSO BE MADE IN LIST2. """
# THERE ARE WAYS TO MAKE A COPY, ONE WAY IS TO USE THE BUILT-IN LIST METHOD COPY().
# MAKE A COPY OF A LIST WITH THE COPY() METHOD:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # OUTPUT: ['apple', 'banana', 'cherry']

# ANOTHER WAY TO MAKE A COPY IS TO USE THE BUILT-IN METHOD LIST().
# MAKE A COPY OF A LIST WITH THE LIST() METHOD:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)  # OUTPUT: ['apple', 'banana', 'cherry']
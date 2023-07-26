# PYTHON - LOOP LISTS

# LOOP THROUGH A LIST
# YOU CAN LOOP THROUGH THE LIST ITEMS BY USING A FOR LOOP.
# EXAMPLE
# PRINT ALL ITEMS IN THE LIST, ONE BY ONE:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# LOOP THROUGH THE INDEX NUMBERS
# YOU CAN ALSO LOOP THROUGH THE LIST ITEMS BY REFERRING TO THEIR INDEX NUMBER.
# USE THE RANGE() AND LEN() FUNCTIONS TO CREATE A SUITABLE ITERABLE.
# EXAMPLE
# PRINT ALL ITEMS BY REFERRING TO THEIR INDEX NUMBER:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# USING A WHILE LOOP
# YOU CAN LOOP THROUGH THE LIST ITEMS BY USING A WHILE LOOP.
""" USE THE LEN() FUNCTION TO DETERMINE THE LENGTH OF THE LIST, THEN START AT 0 AND LOOP YOUR WAY THROUGH THE 
LIST ITEMS BY REFERENCING THEIR INDEXES. """
# REMEMBER TO INCREMENT THE INDEX BY 1 AFTER EACH ITERATION.
# EXAMPLE
# PRINT ALL ITEMS, USING A WHILE LOOP TO GO THROUGH ALL THE INDEXES:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# LOOPING USING LIST COMPREHENSION
# LIST COMPREHENSION OFFERS THE SHORTEST SYNTAX FOR LOOPING THROUGH LISTS:
# EXAMPLE
# A SHORT HAND FOR LOOP THAT WILL PRINT ALL ITEMS IN A LIST:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
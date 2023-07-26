# PYTHON - ACCESS LIST ITEMS

# ACCESS ITEMS
# LIST ITEMS ARE INDEXED AND YOU CAN ACCESS THEM BY REFERRING TO THE INDEX NUMBER:
# PRINT THE SECOND ITEM OF THE LIST:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# NOTE: THE FIRST ITEM HAS INDEX 0.

# NEGATIVE INDEXING
# NEGATIVE INDEXING MEANS START FROM THE END.
# -1 REFERS TO THE LAST ITEM, -2 REFERS TO THE SECOND LAST ITEM ETC.
# PRINT THE LAST ITEM OF THE LIST:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# RANGE OF INDEXES
# YOU CAN SPECIFY A RANGE OF INDEXES BY SPECIFYING WHERE TO START AND WHERE TO END THE RANGE.
# WHEN SPECIFYING A RANGE, THE RETURN VALUE WILL BE A NEW LIST WITH THE SPECIFIED ITEMS.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# NOTE: THE SEARCH WILL START AT INDEX 2 (INCLUDED) AND END AT INDEX 5 (NOT INCLUDED).
# REMEMBER THAT THE FIRST ITEM HAS INDEX 0.

# BY LEAVING OUT THE START VALUE, THE RANGE WILL START AT THE FIRST ITEM:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# BY LEAVING OUT THE END VALUE, THE RANGE WILL GO ON TO THE END OF THE LIST:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# RANGE OF NEGATIVE INDEXES
# SPECIFY NEGATIVE INDEXES IF YOU WANT TO START THE SEARCH FROM THE END OF THE LIST:
# THIS EXAMPLE RETURNS THE ITEMS FROM INDEX -4 (INCLUDED) TO INDEX -1 (EXCLUDED)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# CHECK IF ITEM EXISTS
# TO DETERMINE IF A SPECIFIED ITEM IS PRESENT IN A LIST USE THE IN KEYWORD:
# CHECK IF "APPLE" IS PRESENT IN THE LIST:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
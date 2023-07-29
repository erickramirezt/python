# PYTHON - JOIN SETS

# JOIN TWO SETS
# THERE ARE SEVERAL WAYS TO JOIN TWO OR MORE SETS IN PYTHON
# YOU CAN USE the union() METHOD THAT RETURNS A NEW SET CONTAINING ALL ITEMS FROM BOTH
# SETS, OR THE update() METHOD THAT INSERTS ALL THE ITEMS FROM ONE SET INTO ANOTHER
# EXAMPLE
# THE union() METHOD RETURNS A NEW SET WITH ALL ITEMS FROM BOTH SETS
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# EXAMPLE
# THE update() METHOD INSERTS THE ITEMS IN SET2 INTO SET1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# NOTE: BOTH union() AND update() WILL EXCLUDE ANY DUPLICATE ITEMS

# KEEP ONLY THE DUPLICATES
# THE intersection_update() METHOD WILL KEEP ONLY THE ITEMS THAT ARE PRESENT IN BOTH SETS
# EXAMPLE
# KEEP THE ITEMS THAT EXIST IN BOTH SET x, AND SET y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# THE intersection() METHOD WILL RETURN A NEW SET, THAT ONLY CONTAINS THE ITEMS THAT ARE
# PRESENT IN BOTH SETS
# EXAMPLE
# RETURN A SET THAT CONTAINS THE ITEMS THAT EXIST IN BOTH SETS x, AND SET y
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# KEEP ALL, BUT NOT THE DUPLICATES
# THE symmetric_difference_update() METHOD WILL KEEP ONLY THE ELEMENTS THAT ARE NOT
# PRESENT IN BOTH SETS
# EXAMPLE
# KEEP THE ITEMS THAT ARE NOT PRESENT IN BOTH SETS
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# THE symmetric_difference() METHOD WILL RETURN A NEW SET, THAT CONTAINS ONLY THE
# ELEMENTS THAT ARE NOT PRESENT IN BOTH SETS
# EXAMPLE
# RETURN A SET THAT CONTAINS ALL ITEMS FROM BOTH SETS, EXCEPT ITEMS THAT ARE PRESENT IN
# BOTH
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# NOTE: THE VALUES TRUE AND 1 ARE CONSIDERED THE SAME VALUE IN SETS, AND ARE TREATED AS
# DUPLICATES
# EXAMPLE
# TRUE AND 1 IS CONSIDERED THE SAME VALUE
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

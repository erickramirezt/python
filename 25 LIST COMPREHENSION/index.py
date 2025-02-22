# PYTHON - LIST COMPREHENSION

# LIST COMPREHENSION
""" LIST COMPREHENSION OFFERS THE SHORTEST SYNTAX WHEN YOU WANT TO CREATE A NEW LIST BASED ON THE VALUES OF AN 
EXISTING LIST. """
# EXAMPLE
# BASED ON A LIST OF FRUITS, YOU WANT A NEW LIST, CONTAINING ONLY THE FRUITS WITH THE LETTER "A" IN THE NAME.
# WITHOUT LIST COMPREHENSION YOU WILL HAVE TO WRITE A FOR STATEMENT WITH A CONDITIONAL TEST INSIDE:
# EXAMPLE
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# WITH LIST COMPREHENSION YOU CAN DO ALL THAT WITH ONLY ONE LINE OF CODE:
# EXAMPLE
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# THE SYNTAX
# newlist = [expression for item in iterable if condition == True]
# THE RETURN VALUE IS A NEW LIST, LEAVING THE OLD LIST UNCHANGED.

# CONDITION
# THE CONDITION IS LIKE A FILTER THAT ONLY ACCEPTS THE ITEMS THAT VALUATE TO TRUE.
# EXAMPLE
# ONLY ACCEPT ITEMS THAT ARE NOT "APPLES":
newlist = [x for x in fruits if x != "apple"]
""" THE CONDITION if x != "apple" WILL RETURN TRUE FOR ALL ELEMENTS OTHER THAN "apple", MAKING THE NEW LIST
CONTAIN ALL FRUITS EXCEPT "apple". """

# THE CONDITION IF STATEMENT IS OPTIONAL AND CAN BE OMITTED:
# EXAMPLE
# WITH NO IF STATEMENT:
newlist = [x for x in fruits]

# ITERABLE
# THE ITERABLE CAN BE ANY ITERABLE OBJECT, LIKE A LIST, TUPLE, SET ETC.
# EXAMPLE
# YOU CAN USE THE RANGE() FUNCTION TO CREATE AN ITERABLE:
newlist = [x for x in range(10)]

# SAME EXAMPLE, BUT WITH A CONDITION:
# EXAMPLE
# ACCEPT ONLY NUMBERS LOWER THAN 5:
newlist = [x for x in range(10) if x < 5]

# EXPRESSION
""" THE EXPRESSION IS THE CURRENT ITEM IN THE ITERATION, BUT IT IS ALSO THE OUTCOME, WHICH YOU CAN MANIPULATE
BEFORE IT ENDS UP LIKE A LIST ITEM IN THE NEW LIST: """
# EXAMPLE
# SET THE VALUES IN THE NEW LIST TO UPPER CASE:
newlist = [x.upper() for x in fruits]

# YOU CAN SET THE OUTCOME TO WHATEVER YOU LIKE:
# EXAMPLE
# SET ALL VALUES IN THE NEW LIST TO 'hello':
newlist = ['hello' for x in fruits]

# THE EXPRESSION CAN ALSO CONTAIN CONDITIONS, NOT LIKE A FILTER, BUT AS A WAY TO MANIPULATE THE OUTCOME:
# EXAMPLE
# RETURN "orange" INSTEAD OF "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
# THE EXPRESSION IN THE EXAMPLE ABOVE SAYS:
# "RETURN THE ITEM IF IT IS NOT BANANA, IF IT IS BANANA RETURN ORANGE".
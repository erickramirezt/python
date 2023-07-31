# PYTHON FOR LOOPS

# PYTHON FOR LOOPS
# A FOR LOOPS IS USED FOR ITERATING OVER A SEQUENCE (THAT IS EITHER A LIST, A TUPLE, A DICTIONARY, A SET, OR A
# STRING).
# THIS IS LESS LIKE THE FOR KEYWORD IN OTHER PROGRAMMING LANGUAGES, AND WORKS MORE LIKE AN ITERATOR METHOD AS
# FOUND IN OTHER OBJECT-ORIENTED PROGRAMMING LANGUAGES.
# WITH THE FOR LOOP WE CAN EXECUTE A SET OF STATEMENTS, ONCE FOR EACH ITEM IN A LIST, TUPLE, SET ETC.

# EXAMPLE
# PRINT EACH FRUIT IN A FRUIT LIST:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# LOOPING THROUGH A STRING
# EVEN STRINGS ARE ITERABLE OBJECTS, THEY CONTAIN A SEQUENCE OF CHARACTERS:

# EXAMPLE
# LOOP THROUGH THE LETTERS IN THE WORD "BANANA":
for x in "banana":
    print(x)

# THE BREAK STATEMENT
# WITH THE BREAK STATEMENT WE CAN STOP THE LOOP BEFORE IT HAS LOOPED THROUGH ALL THE ITEMS:

# EXAMPLE
# EXIT THE LOOP WHEN X IS "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# EXIT THE LOOP WHEN X IS "banana", BUT THIS TIME THE BREAK COMES BEFORE THE PRINT:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# THE CONTINUE STATEMENT
# WITH THE CONTINUE STATEMENT WE CAN STOP THE CURRENT ITERATION OF THE LOOP, AND CONTINUE WITH THE NEXT:

# EXAMPLE
# DO NOT PRINT BANANA:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# THE RANGE() FUNCTION
# TO LOOP THROUGH A SET OF CODE A SPECIFIED NUMBER OF TIMES, WE CAN USE THE RANGE() FUNCTION,
# THE RANGE() FUNCTION RETURNS A SEQUENCE OF NUMBERS, STARTING FROM 0 BY DEFAULT, AND INCREMENTS BY 1 (BY 
# DEFAULT), AND ENDS AT A SPECIFIED NUMBER.

# EXAMPLE
# USING THE RANGE() FUNCTION:
for x in range(6):
    print(x)

# NOTE THAT RANGE(6) IS NOT THE VALUES OF 0 TO 6, BUT THE VALUES 0 TO 5.

# THE RANGE() FUNCTION DEFAULTS TO 0 AS A STARTING VALUE, HOWEVER IT IS POSSIBLE TO SPECIFY THE STARTING VALUE BY
# ADDING A PARAMETER: RANGE(2, 6), WHICH MEANS VALUES FROM 2 TO 6 (BUT NOT INCLUDING 6):

# EXAMPLE
# USING THE START PARAMETER:
for x in range(2, 6):
    print(x)

# THE RANGE() FUNCTION DEFAULTS TO INCREMENT THE SEQUENCE BY 1, HOWEVER IT IS POSSIBLE TO SPECIFY THE INCREMENT
# VALUE BY ADDING A THIRD PARAMETER: RANGE(2, 30, 3):

# EXAMPLE
# INCREMENT THE SEQUENCE WITH 3 (DEFAULT IS 1):
for x in range(2, 30, 3):
    print(x)

# ELSE IN FOR LOOP
# THE ELSE KEYWORD IN A FOR LOOP SPECIFIES A BLOCK OF CODE TO BE EXECUTED WHEN THE LOOP IS FINISHED:

# EXAMPLE
# PRINT ALL NUMBERS FROM 0 TO 5, AND PRINT A MESSAGE WHEN THE LOOP HAS ENDED:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# NOTE: THE ELSE BLOCK WILL NOT BE EXECUTED IF THE LOOP IS STOPPED BY A BREAK STATEMENT.

# EXAMPLE
# BREAK THE LOOP WHEN X IS 3, AND SEE WHAT HAPPENS WITH THE ELSE BLOCK:
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# NESTED LOOPS
# A NESTED LOOP IS A LOOP INSIDE A LOOP.
# THE "INNER LOOP" WILL BE EXECUTED ONE TIME FOR EACH ITERATION OF THE "OUTER LOOP":

# EXAMPLE
# PRINT EACH ADJECTIVE FOR EVERY FRUIT:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# THE PASS STATEMENT
# FOR LOOPS CANNOT BE EMPTY, BUT IF YOU FOR SOME REASON HAVE A FOR LOOP WITH NO CONTENT, PUT IN THE PASS 
# STATEMENT TO AVOID GETTING AN ERROR.

# EXAMPLE
for x in [0, 1, 2]:
    pass
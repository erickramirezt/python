# PYTHON LAMBDA

# A LAMBDA FUNCTION IS A SMALL ANONYMOUS FUNCTION.
# A LAMBDA FUNCTION CAN TAKE ANY NUMBER OF ARGUMENTS, BUT CAN ONLY HAVE ONE EXPRESSION.

# SYNTAX
# lambda arguments : expression
# THE EXPRESSION IS EXECUTED AND THE RESULT IS RETURNED:

# EXAMPLE
# ADD 10 TO ARGUMENT a, AND RETURN THE RESULT:
def x(a): return a + 10


print(x(5))

# LAMBDA FUNCTIONS CAN TAKE ANY NUMBER OF ARGUMENTS:

# EXAMPLE
# MULTIPLY ARGUMENT a WITH ARGUMENT b AND RETURN THE RESULT:


def x(a, b): return a * b


print(x(5, 6))

# EXAMPLE
# SUMMARIZE ARGUMENT a, b, AND c AND RETURN THE RESULT:


def x(a, b, c): return a + b + c


print(x(5, 6, 2))

# WHY USE LAMBDA FUNCTIONS?
# THE POWER OF LAMBDA IS BETTER SHOWN WHEN YOU USE THEM AS AN ANONYMOUS FUNCTION INSIDE
# ANOTHER FUNCTION.
# SAY YOU HAVE A FUNCTION DEFINITION THAT TAKES ONE ARGUMENT, AND THAT ARGUMENT WILL BE
# MULTIPLIED WITH AN UNKNOWN NUMBER:


def myfunc(n):
    return lambda a: a * n

# USE THAT FUNCTION DEFINITION TO MAKE A FUNCTION THAT ALWAYS DOUBLES THE NUMBER YOU SEND
# IN:


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))

# OR, USE THE SAME FUNCTION DEFINITION TO MAKE A FUNCTION THAT ALWAYS TRIPLES THE NUMBER
# YOU SEND IN:

# EXAMPLE
def myfunc(n):
    return lambda a: a * n

mytripler = myfunc(3)

print(mytripler(11))

# OR, USE THE SAME FUNCTION DEFINITION TO MAKE BOTH FUNCTIONS, IN THE SAME PROGRAM:

# EXAMPLE
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# USE LAMBDA FUNCTIONS WHEN AN ANONYMOUS FUNCTION IS REQUIRED FOR A SHORT PERIOD OF TIME.


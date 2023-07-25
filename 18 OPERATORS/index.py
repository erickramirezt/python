# PYTHON OPERATORS

# PYTHON OPERATORS
# OPERATORS ARE USED TO PERFORM OPERATIONS ON VARIABLES AND VALUES.
# EXAMPLE
print(10 + 5)

# PYTHON DIVIDES THE OPERATORS IN THE FOLLOWING GROUPS:
# ARITHMETIC OPERATORS
# ASSIGNMENT OPERATORS
# COMPARISON OPERATORS
# LOGICAL OPERATORS
# IDENTITY OPERATORS
# MEMBERSHIP OPERATORS
# BITWISE OPERATORS

# PYTHON ARITHMETIC OPERATORS
# ARITHMETIC OPERATORS ARE USED WITH NUMERIC VALUES TO PERFORM COMMON MATHEMATICAL OPERATIONS:
# OPERATOR  NAME            EXAMPLE
# +         Addition	    x + y
# -         Subtraction	    x - y
# *         Multiplication	x * y
# /         Division	    x / y
# %         Modulus	        x % y
# **        Exponentiation	x ** y
# //        Floor division	x // y

# PYTHON ASSIGNMENT OPERATORS
# ASSIGNMENT OPERATORS ARE USED TO ASSIGN VALUES TO VARIABLES:
# OPERATOR  EXAMPLE     SAME AS
# =	        x = 5	    x = 5
# +=	    x += 3	    x = x + 3
# -=	    x -= 3	    x = x - 3
# *=	    x *= 3	    x = x * 3
# /=	    x /= 3	    x = x / 3
# %=	    x %= 3	    x = x % 3
# //=	    x //= 3	    x = x // 3
# **=	    x **= 3	    x = x ** 3
# &=	    x &= 3	    x = x & 3
# |=	    x |= 3	    x = x | 3
# ^=	    x ^= 3	    x = x ^ 3
# >>=	    x >>= 3	    x = x >> 3
# <<=	    x <<= 3	    x = x << 3

# PYTHON COMPARISON OPERATORS
# COMPARISON OPERATORS ARE USED TO COMPARE TWO VALUES:
# OPERATOR  NAME                        EXAMPLE
# ==	    Equal	                    x == y
# !=	    Not equal	                x != y
# >	        Greater than	            x > y
# <	        Less than	                x < y
# >=	    Greater than or equal to    x >= y
# <=	    Less than or equal to	    x <= y

# PYTHON LOGICAL OPERATORS
# LOGICAL OPERATORS ARE USED TO COMBINE CONDITIONAL STATEMENTS:
# OPERATOR  DESCRIPTION                                                 EXAMPLE
# and	    Returns True if both statements are true	                x < 5 and  x < 10
# or	    Returns True if one of the statements is true	            x < 5 or x < 4
# not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

# PYTHON IDENTITY OPERATORS
""" IDENTITY OPERATORS ARE USED TO COMPARE THE OBJECTS, NOT IF THEY AREA EQUAL, BUT THEY ARE ACTUALLY THE SAME 
OBJECT, WITH THE SAME MEMORY LOCATION: """
# OPERATOR  DESCRIPTION                                                 EXAMPLE
# is	    Returns True if both variables are the same object	        x is y
# is not	Returns True if both variables are not the same object	    x is not y

# PYTHON MEMBERSHIP OPERATORS
# MEMBERSHIP OPERATORS ARE USED TO TEST IF A SEQUENCE IS PRESENT IN AN OBJECT:
# OPERATOR  DESCRIPTION                                                                         EXAMPLE
# in	    Returns True if a sequence with the specified value is present in the object	    x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

# PYTHON BITWISE OPERATORS
# BITWISE OPERATORS ARE USED TO COMPARE (BINARY) NUMBERS:
# OPERATOR  NAME                    DESCRIPTION
# &	        AND	                    Sets each bit to 1 if both bits are 1
# |	        OR	                    Sets each bit to 1 if one of two bits is 1
# ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~	        NOT	                    Inverts all the bits
# <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# OPERATOR PRECEDENCE
# OPERATOR PRECEDENCE DESCRIBES THE ORDER IN WHICH OPERATIONS ARE PERFORMED
# EXAMPLE
# PARANTHESES HAS THE HIGHEST PRECEDENCE, MEANING THAT EXPRESSIONS INSIDE PARANTHESES MUST BE EVALUATED FIRST
print((6 + 3) - (6 + 3))

""" MULTIPLICATION HAS A HIGHER PRECEDENCE THAN ADDITION, AND THEREFOR MULTIPLICATION ARE EVALUATED BEFORE 
ADDITIONS. """
print(6 + 3 * 2)

# THE FOLLOWING TABLE LIST THE OPERATORS IN ORDER OF PRECEDENCE, FROM HIGHEST TO LOWEST:
# OPERATOR                                      DESCRIPTION
# ()                                            Parentheses
# **                                            Exponentiation
# +x, -x, ~x                                    Unary plus, Unary minus
# *, /, %, //                                   Multiplication, Division, Modulus, Floor division
# +, -                                          Addition, Subtraction
# >>, <<                                        Right and Left bitwise shift
# &                                             Bitwise 'AND'
# ^                                             Bitwise 'XOR'
# |                                             Bitwise 'OR'
# ==, !=, >, >=, <, <=, is, is not, in, not in  Comparisons, Identity, Membership operators

# IF TWO OPERATORS HAVE THE SAME PRECEDENCE, PYTHON WILL READ THEM FROM LEFT TO RIGHT
# EXAMPLE
# ADDITION AND SUBTRACTION HAVE THE SAME PRECEDENCE, AND THEREFOR WE EVALUATE THE EXPRESSION FROM LEFT TO RIGHT
print(6 + 3 - 2 + 1)
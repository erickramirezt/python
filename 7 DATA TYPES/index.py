# PYTHON DATA TYPES

# BUILT-IN DATA TYPES
# IN PROGRAMMING, DATA TYPE IS AN IMPORTANT CONCEPT.
# VARIABLES CAN STORE DATA OF DIFFERENT TYPES, AND DIFFERENT TYPES CAN DO DIFFERENT THINGS.
# PYTHON HAS THE FOLLOWING DATA TYPES BUILT-IN BY DEFAULT, IN THESE CATEGORIES:
# TEXT TYPE: STR
# NUMERIC TYPES: INT, FLOAT, COMPLEX
# SEQUENCE TYPES: LIST, TUPLE, RANGE
# MAPPING TYPE: DICT
# SET TYPES: SET, FROZENSET
# BOOLEAN TYPE: BOOL
# BINARY TYPES: BYTES, BYTESARRAY, MEMORYVIEW
# NONE TYPE: NONETYPE

# GETTING THE DATA TYPE
# YOU CAN GET THE DATA TYPE OF ANY OBJECT BY USING THE TYPE() FUNCTION:
# EXAMPLE
x = 5
print(type(x))

# SETTING THE DATA TYPE
# IN PYTHON, THE DATA TYPE IS SET WHEN YOU ASSIGN A VALUE TO A VARIABLE:
# EXAMPLE
x = "Hello World" # STR
x = 20 # INT
x = 20.5 # FLOAT
x = 1j # COMPLEX
x = ["apple", "banana", "cherry"] # LIST
x = ("apple", "banana", "cherry") # TUPLE
x = range(6) # RANGE
x = {"name" : "John", "age" : 36} # DICT
x = {"apple", "banana", "cherry"} # SET
x = frozenset({"apple", "banana", "cherry"}) # FROZENSET
x = True # BOOL
x = b"Hello" # BYTES
x = bytearray(5) # BYTESARRAY
x = memoryview(bytes(5)) # MEMORYVIEW
x = None # NONETYPE

# SETTING THE SPECIFIC DATA TYPE
# IF YOU WANT TO SPECIFY THE DATA TYPE, YOU CAN USE THE FOLLOWING CONSTRUCTOR FUNCTIONS:
# EXAMPLE
x = str("Hello World") # STR
x = int(20) # INT
x = float(20.5) # FLOAT
x = complex(1j) # COMPLEX
x = list(("apple", "banana", "cherry")) # LIST
x = tuple(("apple", "banana", "cherry")) # TUPLE
x = range(6) # RANGE
x = dict(name="John", age=36) # DICT
x = set(("apple", "banana", "cherry")) # SET
x = frozenset(("apple", "banana", "cherry")) # FROZENSET
x = bool(5) # BOOL
x = bytes(5) # BYTES
x = bytearray(5) # BYTESARRAY
x = memoryview(bytes(5)) # MEMORYVIEW

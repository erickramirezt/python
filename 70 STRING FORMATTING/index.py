# PYTHON STRING FORMATTING

# TO MAKE SURE A STRING WILL DISPLAY AS EXPECTED, WE CAN FORMAT THE RESULT WITH THE FORMAT()
# METHOD.

# STRING FORMAT()
# THE FORMAT() METHOD ALLOWS YOU TO FORMAT SELECTED PARTS OF A STRING.
# SOMETIMES THERE ARE PARTS OF A TEXT THAT YOU DO NOT CONTROL, MAYBE THEY COME FROM A 
# DATABASE, OR USER INPUT?
# TO CONTROL SUCH VALUES, ADD PLACEHOLDERS (CURLEY BRACKETS {}) IN THE TEXT, AND RUN THE
# VALUES THROUGH THE FORMAT() METHOD:

# EXAMPLE
# ADD A PLACEHOLDER WHERE YOU WANT TO DISPLAY THE PRICE:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# YOU CAN ADD PARAMETERS INSIDE THE CURLY BRACKETS TO SPECIFY HOW TO CONVERT THE VALUE:

# EXAMPLE
# FORMAT THE PRICE TO BE DISPLAYED AS A NUMBER WITH TWO DECIMALS:
txt = "The price is {:.2f} dollars"

# MULTIPLE VALUES
# IF YOU WANT TO USE MORE VALUES, JUST ADD MORE VALUES TO THE FORMAT() METHOD:
# AND ADD MORE PLACEHOLDERS:

# EXAMPLE
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# INDEX NUMBERS
# YOU CAN USE INDEX NUMBERS (A NUMBER INSIDE THE CURLY BRACKETS {0}) TO BE SURE THE VALUES
# ARE PLACED IN THE CORRECT PLACEHOLDERS:

# EXAMPLE
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# ALSO, IF YOU WANT TO REFER TO THE SAME VALUE MORE THAN ONCE, USE THE INDEX NUMBER:

# EXAMPLE
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# NAMED INDEXES
# YOU CAN ALSO USE NAMED INDEXES BY ENTERING A NAME INSIDE THE CURLY BRACKETS {CARNAME}, BUT
# THEN YOU MUST USE NAMES WHEN YOU PASS THE PARAMETER VALUES TXT.FORMAT(CARNAME = "FORD"):

# EXAMPLE
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
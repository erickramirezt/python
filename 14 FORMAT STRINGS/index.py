# PYTHON - FORMAT - STRINGS

# STRING FORMAT
""" THE FORMAT() METHOD TAKES THE PASSED ARGUMENTS, FORMATS THEM, AND PLACES THEM IN THE STRING WHERE THE 
PLACEHOLDERS {} ARE: """
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# THE FORMAT() METHOD TAKES UNLIMITED NUMBER OF ARGUMENTS, AND ARE PLACED INTO THE RESPECTIVE PLACEHOLDERS:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# YOU CAN USE INDEX NUMBERS {0} TO BE SURE THE ARGUMENTS ARE PLACED IN THE CORRECT PLACEHOLDERS:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
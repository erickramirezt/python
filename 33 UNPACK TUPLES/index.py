# PYTHON - UNPACK TUPLES
# UNPACKING A TUPLE
# WHEN WE CREATE A TUPLE, WE NORMALLY ASSIGN VALUES TO IT. THIS IS CALLED "PACKING" A TUPLE:
# PACKING A TUPLE:
fruits = ("apple", "banana", "cherry")

# BUT, IN PYTHON, WE ARE ALSO ALLOWED TO EXTRACT THE VALUES BACK INTO VARIABLES. THIS IS CALLED "UNPACKING":
# UNPACKING A TUPLE:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)  # OUTPUT: apple
print(yellow)  # OUTPUT: banana
print(red)  # OUTPUT: cherry
# NOTE: THE NUMBER OF VARIABLES MUST MATCH THE NUMBER OF VALUES IN THE TUPLE, IF NOT, YOU MUST USE AN ASTERISK
# TO COLLECT THE REMAINING VALUES AS A LIST.

# USING ASTERISK*
# IF THE NUMBER OF VARIABLES IS LESS THAN THE NUMBER OF VALUES, YOU CAN ADD AN * TO THE VARIABLE NAME AND THE
# VALUES WILL BE ASSIGNED TO THE VARIABLE AS A LIST:
# ASSIGN THE REMAINING VALUES AS A LIST CALLED "RED":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  # OUTPUT: apple
print(yellow)  # OUTPUT: banana
print(red)  # OUTPUT: ['cherry', 'strawberry', 'raspberry']

# IF THE ASTERISK IS ADDED TO ANOTHER VARIABLE NAME THAN THE LAST, PYTHON WILL ASSIGN VALUES TO THE VARIABLE
# UNTIL THE NUMBER OF VALUES LEFT MATCH THE NUMBER OF VARIABLES LEFT.
# ADD A LIST OF VALUES THE "TROPICAL" VARIABLE:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropical, red) = fruits
print(green)  # OUTPUT: apple
print(tropical)  # OUTPUT: ['mango', 'papaya', 'pineapple']
print(red)  # OUTPUT: cherry

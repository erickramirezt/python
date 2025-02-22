# ASSIGN MULTIPLE VALUES

# MAANY VALUES TO MULTIPLE VARIABLES
# PYTHON ALLOWS YOU TO ASSIGN VALUES TO MULTIPLE VARIABLES IN ONE LINE
# EXAMPLE
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# MAKE SURE THE NUMBER OF VARIABLES MATCHES THE NUMBER OF VALUES, OR ELSE YOU WILL GET AN ERROR

# ONE VALUE TO MULTIPLE VARIABLES
# AND YOU CAN ASSIGN THE SAME VALUE TO MULTIPLE VARIABLES IN ONE LINE
# EXAMPLE
x = y = z = "Orange"
print(x)
print(y)
print(z)

# UNPACK A COLLECTION
""" IF YOU HAVE A COLLECTION OF VALUES IN A LIST, TUPLE ETC. PYTHON ALLOWS YOU EXTRACT 
THE VALUES INTO VARIABLES. THIS IS CALLED UNPACKING """
# EXAMPLE
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# PYTHON POLYMORPHISM

# THE WORD POLYMORPHISM MEANS HAVING MANY FORMS, AND IN PROGRAMMING IT REFERS TO METHODS/
# FUNCTIONS/OPERATORS WITH THE SAME THAT CAN BE EXECUTED ON MANY OBJECTS OR CLASSES

# FUNCTION POLYMORPHISM
# AN EXAMPLE OF A PYTHON FUNCTION THAT CAN BE USED ON DIFFERENT OBJECTS IS THE LEN()
# FUNCTION

# STRING
# FOR STRINGS LEN() RETURNS THE LENGTH OF THE STRING

# EXAMPLE
x = "Hello World"
print(len(x))

# TUPLE
# FOR TUPLES LEN() RETURNS THE LENGTH OF THE TUPLE

# EXAMPLE
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

# DICTIONARY
# FOR DICTIONARIES, LEN() RETURNS THE NUMBER OF ITEMS IN THE DICTIONARY

# EXAMPLE
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(len(thisdict))

# CLASS POLYMORPHISM
# POLYMORPHISM IS OFTEN USED IN CLASS METHODS, WHERE WE CAN HAVE MULTIPLE CLASSES WITH THE
# SAME METHOD NAME
# FOR EXAMPLE, SAY WE HAVE THREE CLASSES: CAR, BOAT, AND PLANE, AND THEY ALL HAVE A METHOD
# NAMED MOVE()

# EXAMPLE
# DIFFERENT CLASSES WITH THE SAME METHOD


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")
boat = Boat("Bayliner", "175")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    x.move()

# LOOK AT THE FOR LOOP AT THE END. BECAUSE OF POLYMORPHISM WE CAN EXECUTE THE SAME METHOD
# FOR ALL THREE CLASSES

# INHERITANCE CLASS POLYMORPHISM
# WHAT ABOUT CLASSES WITH CHILD CLASSES WITH THE SAME NAME? CAN WE USE POLYMORPHISM THERE?
# YES, IF WE USE THE EXAMPLE ABOVE AND MAKE A PARENT CLASS CALLED VEHICLE, AND MAKE CAR,
# BOAT, PLANE CHILD CLASSES OF VEHICLE, THE CHILD CLASSES INHERITS THE VECHICLE METHODS,
# BUT CAN OVERRIDE THEM

# EXAMPLE
# CREATE A CLASS CALLED VEHICLE AND MAKE CAR, BOAT, PLANE CHILD CLASSES OF VEHICLE


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car = Car("Ford", "Mustang")
boat = Boat("Bayliner", "175")
plane = Plane("Boeing", "747")

for x in (car, boat, plane):
    print(x.brand, x.model)
    x.move()

# CHILD CLASSES INHERITS THE PROPERTIES AND METHODS FROM THE PARENT CLASS
# IN THE EXAMPLE ABOVE YOU CAN SEE THAT THE CAR CLASS IS EMPTY, BUT IT INHERITS BRAND, 
# MODEL, AND  MOVE() FROM VEHICLE
# THE BOAT AND PLANE CALSSES ALSO INHERIT BRAND, MODEL, AND MOVE() FROM VEHICLE, BUT THEY 
# BOTH OVERRIDE THE MOVE() METHOD
# BECAUSE OF POLYMORPHISM WE CAN EXECUTE THE SAME METHOD FOR ALL CLASSES
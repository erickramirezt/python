# PYTHON - SORT LISTS

# SORT LIST ALPHANUMERICALLY
# LIST OBJECTS HAVE A SOTR() METHOD THAT WILL SORT THE LIST ALPHANUMERICALLY, ASCENDING, BY DEFAULT:
# EXAMPLE
# SORT THE LIST ALPHABETICALLY:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# EXAMPLE
# SORT THE LIST NUMERICALLY:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# SORT DESCENDING
# TO SORT DESCENDING, USE THE KEYWORD ARGUMENT reverse = True:
# EXAMPLE
# SORT THE LIST DESCENDING:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# EXAMPLE
# SORT THE LIST DESCENDING:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)

# CUSTOMIZE SORT FUNCTION
# YOU CAN ALSO CUSTOMIZE YOUR OWN FUNCTION BY USING THE keyword argument key = function.
# THE FUNCTION WILL RETURN A NUMBER THAT WILL BE USED TO SORT THE LIST (THE LOWEST NUMBER FIRST):
# EXAMPLE
# SORT THE LIST BASED ON HOW CLOSE THE NUMBER IS TO 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# CASE INSENSITIVE SORT
""" BY DEFAULT THE SORT() METHOD IS CASE SENSITIVE, RESULTING IN ALL CAPITALIZED LETTERS BEING SORTED BEFORE 
LOWER CASE LETTERS: """
# EXAMPLE
# CASE SENSETIVE SORTING CAN GIVE UNEXPECTED RESULT:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# LUCKILY WE CAN USE BUILT-IN FUNCTIONS AS KEY FUNCTIONS WHEN SORTING A LIST.
# SO IF YOU WANT A CASE-INSENSITIVE SORT FUNCTION, USE str.lower AS A KEY FUNCTION:
# EXAMPLE
# PERFORM A CASE-INSENSITIVE SORTING:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# REVERSE ORDER
# WHAT IF YOU WANT TO REVERSE THE ORDER OF A LIST, REGARDLESS OF THE ALPHABETICAL ORDER?
# THE REVERSE() METHOD REVERSES THE CURRENT SORT ORDER OF THE ELEMENTS:
# EXAMPLE
# REVERSE THE ORDER OF THE LIST ITEMS:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
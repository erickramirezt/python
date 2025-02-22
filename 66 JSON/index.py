# PYTHON JSON

# JSON IS A SYNTAX FOR STORING AND EXCHANGING DATA
# JSON IS TEXT, WRITTEN WITH JAVASCRIPT OBJECT NOTATION

# JSON IN PYTHON
# PYTHON HAS A BUILT-IN PACKAGE CALLED JSON, WHICH CAN BE USED TO WORK WITH JSON DATA

# EXAMPLE
# IMPORT THE JSON MODULE
import json

# PARSE JSON - CONVERT FROM JSON TO PYTHON
# IF YOU HAVE A JSON STRING, YOU CAN PARSE IT BY USING THE json.loads() METHOD

# THE RESULT WILL BE A PYTHON DICTIONARY

# EXAMPLE
# CONVERT FROM JSON TO PYTHON
x = '{ "name":"John", "age":30, "city":"New York"}'

# PARSE X
y = json.loads(x)

# THE RESULT IS A PYTHON DICTIONARY
print(y["age"])

# CONVERT FROM PYTHON TO JSON
# IF YOU HAVE A PYTHON OBJECT, YOU CAN CONVERT IT INTO A JSON STRING BY USING THE
# json.dumps() METHOD

# EXAMPLE
# A PYTHON OBJECT (DICT)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# CONVERT INTO JSON
y = json.dumps(x)

# THE RESULT IS A JSON STRING
print(y)

# YOU CAN CONVERT PYTHON OBJECTS OF THE FOLLOWING TYPES, INTO JSON STRINGS
# DICT
# LIST
# TUPLE
# STRING
# INT
# FLOAT
# TRUE
# FALSE
# NONE

# EXAMPLE
# CONVERT A PYTHON OBJECTS INTO JSON STRINGS, AND PRINT THE VALUES
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# WHEN YOU CONVERT FROM PYTHON TO JSON, PYTHON OBJECTS ARE CONVERTED INTO THE JSON
# (JAVA SCRIPT) EQUIVALENT
# PYTHON    JSON
# DICT      OBJECT
# LIST      ARRAY
# TUPLE     ARRAY
# STR       STRING
# INT       NUMBER
# FLOAT     NUMBER
# TRUE      TRUE
# FALSE     FALSE
# NONE      NULL

# EXAMPLE
# CONVERT A PYTHON OBJECT CONTAINING ALL THE LEGAL DATA TYPES
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))

# FORMAT THE RESULT
# THE EXAMPLE ABOVE PRINTS A JSON STRING, BUT IT IS NOT VERY EASY TO READ, WITH NO 
# INDENTATIONS AND LINE BREAKS
# THE json.dumps() METHOD HAS PARAMETERS TO MAKE IT EASIER TO READ THE RESULT

# EXAMPLE
# USE THE INDENT PARAMETER TO DEFINE THE NUMBER OF INDENTATIONS
print(json.dumps(x, indent=4))

# YOU CAN ALSO DEFINE THE SEPARATORS, DEFAULT VALUE IS (", ", ": "), WHICH MEANS USING
# A COMMA AND A SPACE TO SEPARATE EACH OBJECT, AND A COLON AND A SPACE TO SEPARATE KEYS
# FROM VALUES

# EXAMPLE
# USE THE SEPARATORS PARAMETER TO CHANGE THE DEFAULT SEPARATOR
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# ORDER THE RESULT
# THE json.dumps() METHOD HAS PARAMETERS TO ORDER THE KEYS IN THE RESULT

# EXAMPLE
# USE THE sort_keys PARAMETER TO SPECIFY IF THE RESULT SHOULD BE SORTED OR NOT
print(json.dumps(x, indent=4, sort_keys=True))

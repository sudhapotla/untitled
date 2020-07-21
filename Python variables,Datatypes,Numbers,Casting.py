#Python Variables
#Variables are containers for storing data values.
#Rules for Variable names
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
my_name="sudha"
address="westchester"
print(my_name)
print(address)
#python uses + character to combine the text and variable
print(my_name + " lives in "+ address )
#If you try to combine a string and a number, Python will give you an error:
"""my_name="sudha"
address= 114
print(my_name + " lives in "+ address )"""
#Global variables
#Variables that are created outside of a function
#Global variables can be used by everyone, both inside of functions and outside.
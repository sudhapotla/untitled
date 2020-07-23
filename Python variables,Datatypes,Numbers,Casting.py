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
x= "python"
y= " is awesome"
z= (x+y)
print(z)
#Global variables created outside a fnction
x= "awesome"
def myfunc():
    print("python is" + x)
  #creating a variable inside the function with the same name as the global variable
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
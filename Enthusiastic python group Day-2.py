# Output Variables
# python uses + character to combine both text and Variable
x = ("hard ")
print("we need to work " + x)
x = ("hardwork is the ")
y = (" key to success")
z = (x + y)
print(z)

#Create a variable outside of a function, and use it inside the function

x = "not stressfull"

def myfunc():
  print("Python is " + x)

myfunc()
# Create a variable inside a function, with the same name as the global variable
x = "not stressfull"

def myfunc():
    x = "may be sometimes hard"
    print("python  " + x)

myfunc()
print("python is " + x)
# To create a global variable inside a function, you can use the global keyword
def myfunc():
    global x
    x = "easy"
myfunc()

print ("python is "+ x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "easy"
def myfunc():
    global x
    x = "hard"
myfunc()
print("python is " + x)

# Learning DataTypes
x = 9
print(type(x))
x = " is everybody's lucky number"  # str
print(type(x))
x = 20.5
print(type(x))
x = 1j
print(type(x))
x = ["sarees", "blouses", "dresses"]
print(type(x))
x = ("gavvalu", "chekkalu", "kova")
print(type(x))
x = range(7)
print(type(x))
x = {"name": "Pluto", "age": 12}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = True
print(x)
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(x)
print(type(x))
x = memoryview(bytes(5))
print(type(x))

# Learning Python numbers
# Integers
x = 7
y = 35656222554887711
z = -67890

print(type(x))
print(type(y))
print(type(z))
#Float
x = 2.10
y = 7.0
z = -36.59

print(type(x))
print(type(y))
print(type(z))

#Complex
x= 1j
y= 7+5j
z= -5j
print(type(x))
print(type(x))
print(type(x))

# converting from one type to another with the int(), float(), and complex() methods:
x = 1        #int
y = 2.5      #float
z = 1+5j     #complex
# convert from int to float

a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)                   #cannot convert complex numbers into another number type.


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
 # Random numbers
#Python does not have a random() function to make a random number, but Python has a built-in module
#called random that can be used to make random numbers:
import random
import random

print(random.randrange(2, 100))







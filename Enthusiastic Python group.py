# print () function
print("Friends started learning Python from today!")
# indentataion
print(" we set goals to learn until variables!")
print(" we set goals to learn until variables!")
# Comments
print("should use the hash # symbol not to execute the the function!")
# Assigning values to the variable
x = " it is interesting and fun learning as of todays class"
y = " down the lane should see how it goes"
print(x, y)
y = (" but it's interesting")
print(y)
# Assigning string values to multiple variables
variable1 = "I think I'm going to be busy"
variable_1 = " relatives are coming this weekend"
_variable_1 = "and on the 10th of july they are leaving to India"
variable_2 = "including my mother-in-law!"
print(variable1, variable_1, _variable_1, variable_2)
# changing the values to variable_2
variable_2 = " need to do some necessary shopping and help in packing"
print(variable_2)
# Assigning the same value to multiple variables in a single line
a = b = c = "I'm happy learning with kiran and padmaja"
print(a)
print(b)
print(c)
b = c = "Finally did my homework haha"
print(b, c)
c = " I'll take rest now bye"
print(c)
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
print(type(x))      #int

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
x = {"name" : "Pluto", "age" : 12}
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




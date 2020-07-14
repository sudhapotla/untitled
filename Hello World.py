print("Hello world!")

# Indentation
if 5 > 2:
  print("Five is greater than two!")
if 5 > 2:
 print("five greater than two!")
#This is a comment
print("Hello, World!")
print("Hello,world!")
#This is a comment
#written in
#more than just one line
print("Hello, World!")
# creating Varibles
x = 5
y = "sudha"
print(x)
print(y)
myname = "sudha"
my_friend ="padmaja"
_my_friend ="kiran"
mysister = "Madhuri"
MYDAD = "Gopalakrishniah"
mymom2 ="Radhamani"
print(myname,my_friend,_my_friend,mysister,MYDAD,mymom2)
x, y, z = "This", "is", "Venu"
print(x)
print(y)
print(z)
x=y=z=1
print(x)
print(y)
print(z)
x=2
print(x)
# Day2
x = "awesome"
print("python is" +  x)
y= "python is "
x="awesome"
z = (y + x)
print(z)
#Mathematical operator addition
x=5
y=10
print(x+y)
#combining string and number
x="john"
y= 5
#z= (x+y)
#Global Variables
a="awesome"
def myfun():

    print(" python is " + a)
myfun()
#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global a
a = "fantastic"

myfunc()

print("Python is " + a)
#Day-3
#python casting using constructor functions
# Integers
x = int(10)
y = int(2.1)
z = int("5")
print(x,y,x*5)
# Array of characters
a = "Hello, world!"
print(a[5])
#slicing
b = "Hello, World!"
print(b[2:5])
# String length
a = "Hello, World!"
print( "length of the string is",len(a))     # length function
# string methods
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# Split string
a = " Hello, world!"
print(a.split(","))
a = "Hello,world abc"
print(a.split(","))
# Checkinng the string
txt = "My name is Sudha"
x = "is" in txt
print(x)
#Day4
#string format
#age = 36
#txt = "My name is sudha, I am " + age
#print(txt)
age = 36
txt = "My name is sudha, and I am {}" #format method
print(txt.format(age))
#Boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 100
b = 20
if b < a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print(bool("Hello"))
print(bool(15))
x = ""
y = 0

print(bool(x))
print(bool(y))
def myFunction() :
  return 0
print(bool(myFunction()))

a =10
b =20
if b>a:
    print (bool(a))
else:
    print (bool(b))
txt = "hi going out"
x1  = txt.center(15,"*")
print(x1)
txt = "hi going out"
y= txt.encode()
print(y)
point = {'x':2,'y':4}
print("(x,y) is ,"'{x},{y}'.format_map(point))
print("Hi friends,thx so much for your cooperation!")
#python indentation
if 5>2:
    print("five is greater than two!")
if 6<10:
 print("six is less than ten!")
 #python variables
 x = 3
 y = "Thank you friends"
 print(x)
 print(y)
 #string variables
 x = "sudha"
 print(x)
 #variable names
 myname = "sudha1"
 myname2 = "sudha2"
 my_name ="sudha3"
 _myname ="sudha4"
 print(myname,myname2,my_name,_myname)
 #assigning values to multiple variables
 a,b,c = "gulabjamoon" ,"mysurpak" ,"kalakand"
 print(a)
 print(b)
 print(c)
 #assigning the same value to multiple variables in one line
 a=b=c='mysurpak'
 print(a)
 print(b)
 print(c)
 #output variables, combing the text and the variable
 a="mysurpak"
 print("I love "+ a)
 #adding variable to another variable
 b="I love"
 a="mysurpak"
 c=(b+a)
 print(c)
 #For numbers, the + character works as a mathematical operator:
 x =5
 y =10
 z= x+y
 print(z)
#note combining a string and a number will give an error
#x = 5
#y = "John"
#print(x + y)
#Global variables
x ="mysurpak"
def myfunc():
  print("I love " + x)

myfunc()
#Creating a variable inside a function, with the same name as the global variable
x ="mysurpak"
def myfunc():
 x= "kalakand"
 print(" I love " + x)
 myfunc()

 print("I love " + x)
 #using global keyword ,To create a global variable inside a function, you can use the global keyword.
 def myfunc():
     global x
     x = "mysurpak"

 myfunc()

 print("I love " + x)
 #To change the value of a global variable inside a function, refer to the variable by using the global keyword:
 x = "awesome"

 def myfunc():
     global x
     x = "fantastic"

 myfunc()

 print("Python is " + x)
#using comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")



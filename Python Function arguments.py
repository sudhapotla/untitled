#python Functions
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("hi", name + ', ' + msg)
greet("Kiran", "Good morning!")
greet("Kiran","Good morning")
#greet()
def greet(name, msg="True friends are rare!"):
    """
    This function greets the friends nature
    If the message is not provided,
    it defaults to "Good
    morning!"
    """
    print("Hello", name + ', ' + msg)
greet("kiran")
greet("kiran","True friends are rare")
greet(name="Kiran", msg = "True friends are rare!" )
#calling a function
#To call a function, use the function name followed by parenthesis:
def my_function():
  print("True friends are rare")
my_function()
#Arguments
#Information can be passed into functions as arguments.
#Arguments are specified after the function name,
# inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
def my_function(fname):
  print(fname + " girl")
my_function("kiran")
my_function("padmaja")
my_function("madhuri")
"""#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments,
# you have to call the function with 2 arguments, not more, and not less."""
def my_function(fname,lname):
    print(fname + " " +lname)
my_function("sudha" ,"potla")
def my_function(fname,lname):
    print(fname + " " + lname)
#my_function("sudha")#If you try to call the function with 1 or 3 arguments, you will get an error:
 #def no_arg_greet():
  #  print("Hello friends are you enjoying python?")
  #recursion
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 2:
        return 2
    else:
        return (x * factorial(x - 1))
num = 4
print("The factorial of", num, "is", factorial(num))
#passing list
def my_list(groceries):
    for x in groceries:
        print(x)
        items=["milk","eggs","cheese"]
        my_list(items)
#passing multiple names
def my_function(*friends):
     print("friend whose last name" + friends[2])
     my_function("potla","botla","lanka")










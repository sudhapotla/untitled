a=5
b=-10
c=1.5
if a>0:
    print("a is positive")
else:
    print("a is negative")

if a>=3:
 print("a=",a)

elif a<3:
  print("a=",a)
if a>3 and a<10:

 if a<b:

  print("a=",a)

elif a>b:
   print("b=",b)

x=True
if x is False:
    print("x is not true")
elif x:
    print("x is true")
#using if keyword
a=33
b=200
if b>a:
    print("b is greater than a")
#using else keyword
a=100
b=50
if b>a:
    print("b is greater than a")
else:
    print("b is not greateer than a")

 #If statement, without indentation (will raise an error):
#a = 33
#b = 200
#if b > a:
#print("b is greater than a")
#using elif keyword
a=33
b=200
if b>a:
    print("b is greater than a")
elif  a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
#using else keyword
a=200
b=33
if b>a: print("b is greater than a")
else:
  print("b is not greater than a")
  #shorthand if
  if a > b: print("a is greater than b")
  #shorthand if else
a = 33
b = 200
print("a") if (a>b)else print("b")
#if statement with 3 conditions
print("a")if a>b else ("=")if a==b else print("b")
#using AND keyword
a= 33
b= 200
c=100
if a<b and c<b:
    print("both conditions are true")
#using or
if a<c or a>b:
    print("atleast one condition is true")
#Nested if
x = 61

if x > 20:
  print("Above 20,")
  if x > 30:
    print("and also above 30!")
  else:
    print("but not above 20.")
#pass statement
a = 33
b = 200
if b > a:
    pass
# more if variations
num=3
#num = -5
#num= 0
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")
#example of if eleif

num = 5.4

# Try these two variations as well:
# num = 0
# num = -4.5

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
#using nested if
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")



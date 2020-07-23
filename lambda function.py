#lambda functions
# Program to filter out even  items from a list
number_list = [1, 5, 4, 7, 8, 11, 3, 13]
odd_list = list(map(lambda x: (x*2 ) , number_list))
print(odd_list)
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression
#lambda arguments : expression
#subtraction
x = lambda a : a - 10
print(x(5))
#lambda taking multiple arguments
x= lambda a,b,c: a*b*c
print(5*6*3)
#Use  function definition to make a function that always doubles the number
def myfunc(n):
    return lambda a : a * 10
mymul=myfunc(10)
print(mymul(50))
def myfunc(n):
    return lambda a : a +10
myadd=myfunc(10)
print(myadd(50))
#using same function to make both the funtions






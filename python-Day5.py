#python operators
#addition
x=10
y=5
print(x+5)
#substraction
x=10
y=5
#multiplicatopm
print(x-5)
x=10
y=5
print(x*5)
#Division
x=10
y=5
print(x/5)
#modulus
x=10
y=5
print(x%5)
#exponentation
x=10
y=5
print(x**5)
#floor division
x=10
y=5
print(x//5)
#python assignment operators
x =5
print(x)
x = 5
x += 3
print(x)
x = 5
x -= 3
print(x)
x = 5
x *= 3
print(x)
x = 5
x /= 3
print(x)
x = 5
x %= 3
print(x)
x = 5
x //= 3
print(x)
x = 5
x **= 3
print(x)
x = 5
x &= 3
print(x)
x = 5
x |= 3
print(x)
x = 5
x ^= 3
print(x)
x = 5
x >>= 3
print(x)
x = 5
x<<= 3
print(x)
# python comparison operators
x= 5
y= 3
print(x==y)
# returns False because 5 is not equal to 3
x = 5
y = 3
print(x != y)
# returns true because 5 is not equal to 3
x = 5
y = 3
print(x > y)
# returns true because 5 is greater than 3
x = 5
y = 3
print(x < y)
# returns false because 5 is greater than 3
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3
#python logical operators
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10
x = 5
print(x < 3 or x < 4)
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result
#python identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#python membership operators
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list













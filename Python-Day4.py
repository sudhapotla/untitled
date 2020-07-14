#we can combine strings and numbers by using the format() method!
age = 12
txt = "My name is Pluto, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments
dresses = 3
dresscode = 999
price = 60.0
myorder = "I want {} dresses with dresscode {} for {} dollars."
print(myorder.format(dresses, dresscode, price))
# using index numbers
dresses = 3
dresscode = 999
price = 60.0
myorder = "I want {0} dresses with dresscode {1} for {2} dollars."
print(myorder.format(dresses, dresscode, price))
#Escape characters
txt = "I want 3 dresses with \"dresscode\" 999 for 60.0 dollars." # using backslash
print(txt)
txt = 'what\'s your name.'
print(txt)
txt = "what's your \\(name)."
print(txt)
txt = "what's \n your (name)."
print(txt)
txt = "what's \t your name."
print(txt)
txt = "what's \r\n your name."
print(txt)
txt = "what's \byour name."
print(txt)
txt = "\110\145\154\154\157"
print(txt)
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#the iinstance() function
x = 3
print(isinstance(x, int))
x = 3.0
print(isinstance(x, float))
x = 3
print(isinstance(x, str))
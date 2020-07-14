#Python Casting using constructors( specifying a variable)
x = float(2.1)
y = float(2)
z = float("4.1")   #float
w = float("6")
print(x,y,z,w)
x = str("s2")
y = str(5)       #string
z = str(4.0)
print(x,y,z)
#Python String literals
print("sairam")
print('sairam')
#Multiline strings
a = """ tomorrow is thursday which is shiridi sai day
love the song sai saranam baba saranam and his teaching 
say shraddha and   can acheive everyhting.
"""
print(a)
b = '''tomorrow is thursday which is shiridi sai day
love the song sai saranam baba saranam and his teaching 
say shraddha and   can acheive everyhting.'''
print(b)
#Negative indexing
c= "tommorow is, thursday!"
print(c[-5:-2])
#string methods
a = "Tomorrow Is Thursday!"  #lower
print(a.lower())
b= "Tomorrow Is Thursday!"  #upper
print(b.upper())
a = "Tomorrow is, Thursday!" # replace
print(a.replace("T", "k"))
txt = "tomorrow is thursday" #check
x = "is" in txt
print(x)
txt = "tomorrow is thursday" #check
x = "is"  not in txt
print(x)
a = "Tomorrow is "
b = "Thursday"    #string concatenation
c = a + b
print(c)
a = "tomorrow is"
b = "thursday"   #adding a space
c = a + " " + b
print(c)
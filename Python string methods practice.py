#String methods
a= " All the three friends are practicing string methods today"
print(a)
print(a.capitalize())
print(a.casefold())
txt="  three friends "
print(txt.center(40))
txt= "All the three friends and three more friends"
x= txt.count("three")
print(x)
txt="All the three friends"
x=txt.encode()
print(x)
txt=" All the three friends are practicing string methods today."
x=txt.endswith(".")
print(x)
txt= "A\l\l"
x=txt.expandtabs(2)
print(x)
text= " All the three friends are practicing string methods today."
x=txt.find("practicing")
print(x)
age=45
txt=" All the three friends are practicing python  and not any language and they are{}"
x=txt.format( age)
print(x)
txt= " All the three friends are practicing string methods today."
x=txt.format_map("friends")
print(x)



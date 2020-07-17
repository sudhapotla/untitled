#creating a dictionary
thisdict = {
  "brand": "Audi",
  "model": "Q5",
  "year": 2014
}
print(thisdict)
#accessing the values using the key name with []
x = thisdict["model"]

print(x)
x = thisdict.get("model")
print(x)
#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:

thisdict = {
  "brand": "audi",
  "model": "Q5",
  "year": 2014
}
thisdict["year"] = 2018
print(thisdict)
#printing all the keyvalues in thee dictionary
for x in thisdict:
  print(x)
  #Loop through both keys and values, by using the items() method:
  for x, y in thisdict.items():
      print(x, y)

#use the in keyword to check if key exists
thisdict = {
  "brand": "audi",
  "model": "Q5",
   "year":  2014
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#length of the dictionary
print(len(thisdict))
#adding items
thisdict = {
  "brand": "audi",
  "model": "Q5",
  "year": 2014
}
thisdict["color"] = "blue"
print(thisdict)
#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "audi",
  "model": "Q5",
  "year": 2014
}
thisdict.pop("model")
print(thisdict)
#The popitem() method removes the last inserted item
thisdict = {
  "brand": "audi",
  "model": "Q5",
  "year": 2014
}
thisdict.popitem()
print(thisdict)
#using del keyword
del thisdict["model"]
print(thisdict)
#using clear keyword
thisdict.clear()
print(thisdict)
#using copy method you can copy dictionary
thisdict = {
  "brand": "audi",
  "model": "Q5",
  "year": 2014
}
mydict = thisdict.copy()
print(mydict)
#using a dictionary ()function you can copy dictionary
mydict = dict(thisdict)
print(mydict)
#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Neha",
    "year" : 2004
  },
  "child2" : {
    "name" : "Rohan",
    "year" : 2006
  },
  "child3" : {
    "name" : "Pluto",
    "year" : 2019
  }
}
print(myfamily)
#creating 3dictionaries
child1 = {
  "name" : "Neha",
  "year" : 2004
}
child2 = {
  "name" : "Rohan",
  "year" : 2007
}
child3 = {
  "name" : "Pluto",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#using dic() constrructor
thisdict = dict(brand="audi", model="Q5", year=2014)
print(thisdict)
# using method update
d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d)

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d)
#using from keys
# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }

vowels = dict.fromkeys(keys)
print(vowels)


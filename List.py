#list
thislist = ["apple", "banana", "cherry"]
print(thislist)
#list with index
thislist=["sudha","kiran","Padmaja"]
print(thislist[1])
#Negative indexing
thislist=["pluto","Bruno","Arlo"]
print(thislist[-1])
#Range of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:7])
#returns the items from the beginning
thislist=["sudha","kiran","Padmaja"]
print(thislist[:2])
#returns the items to the end
thislist=["sudha","kiran","Padmaja"]
print(thislist[0:])
#range of negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#change item value
thislist=["sudha","kiran","Padmaja"]
thislist[1]="Madhuri"
print(thislist)
#loop through a list using for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#to check if the particular item exists using in Keyword
thislist = ["apple", "banana", "cherry"]
if "banana" in thislist:
  print("Yes, 'banana' is in the fruits list")
#list length using len() function
thislist= ["amma","nannagaru","akka"]
print(len(thislist))
#adding the items using append() method
thislist=["Neha","Rohan","Venu"]
thislist.append("Sudha")
print(thislist)
#adding the items using insert() method for a specific index
thislist=["Neha","Rohan","Venu"]
thislist.insert(1,"Sudha")
print(thislist)
#using remove method() you can remove the specific item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#using the pop() you can remove the specified index
thislist = ["apple", "banana", ]
thislist.pop()
print(thislist)
#using the del keyword
thislist = ["apple", "banana", "cherry"]
del thislist[2]
print(thislist)
#using the del keyword to delete the complete list
#thislist = ["apple", "banana", "cherry"]
#del thislist
#print(thislist)
#using the clear()
thislist=["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#copy list with copy()
thislist = ["apple", "Mango", "cherry"]
mylist = thislist.copy()
print(mylist)
#another way to copy a list is to use a built in method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#joining two lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#Another way to join two lists are by appending all the items from list2 into list1, one by one:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
# using the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# using the list constructor to make the list
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#sets
thisset={1,2,3.2,4.2,"hello"}
print(thisset)
#thisset={3+2j,(2,4),{2+2}}
#print(thisset)
#thisset={{"name":"sudha"}}
#print(thisset)
a={}
print(type(a))
a=set()
print(type(a))
a=set()
print(a)
thisset={1,2,3.2,4.2,"hello"}
for x in thisset:
    print(x)
    print(type(x))
#different types of sets in python
myset={"sudha","kiran","padmaja"}
print(myset)
#emptyset
#myset={}
#print(myset)
#print(type(myset))
#myset=set()
#print(type(myset))
#add method
myset.add("Madhuri")
print(myset)
#update method
myset.update(["pluto","Bruno"])
print(myset)
myset.update([1,2,3])
print(myset)
#discaard/remove
myset.discard(1)
print(myset)
myset.remove(2)
print(myset)
myset.discard(3)
print(myset)
#myset.remove(3)
#print(myset)
#pop method
print(myset.pop())
myset.pop()
print(myset)
myset.clear()
print(myset)
#python set operations
a= {"green","yellow","pink","blue"}
b = {"white","black","orange","purple"}
print(a|b)
a.union(b)
b.union(a)
print(a|b)
#intersection
a={"green","yellow","pink"}
b={"green","black","orange"}
print(a&b)
a.intersection(b)
b.intersection(a)
result=a.intersection_update(b)
print(result)
#
print(a&b)
print(a-b)
a={1, 2, 3,4,5,6}
b={4,5,6,7,8,9,10}
print(a-b)
print(a.difference(b))
print(b.difference(b))
#differnece_update
result =a.difference_update()
print(result)
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}
result = C.intersection_update(B, A)
print('result =', result)
print('C =', C)
print('B =', B)
print('A =', A)
#symmetrric difference
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
A.symmetric_difference(B)
print(A ^ B)
result=A.symmetric_difference_upate()







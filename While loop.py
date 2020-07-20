#while loop
i = 1
while i < 6:
  print(i)
  i += 1
#break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  #continue statement
#learning while loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  #else statement
  i = 1
  while i < 6:
      print(i)
      i += 1
  else:
      print("i is no longer less than 6")
#knowing if the number is even or odd in Python
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
#python program to find the prime numberrs using while

Number = int(input(" Please Enter any Number: "))
count = 0
i = 2

while (i <= Number // 2):
    if (Number % i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" % Number)
else:
    print(" %d is not a Prime Number" % Number)

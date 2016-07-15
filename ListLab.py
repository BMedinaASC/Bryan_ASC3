#1
myList = range(10, 21)
print (myList)

x = 10
myList1 = []

for i in range (10, 21): 
    myList1.append(x)
    x = x + 1
    
print (myList1)

#2/4
myList2 = []

for j in range (5):
    myList2.append(0)
    
print(myList2)    

#3
emptyList = []
print(emptyList)

#5
myList5 = ["a", 5, "doodle", 3, 10]
print(len(myList5))

#6
del myList5[3]
print(myList5)

#7
myList5.append("lol")
print(myList5)

#8
myList5[0] = 8.4
print(myList5)

#9
myList5.insert(0, "roflcopter")
print(myList5)

#10
myOddList = []
y = 1
for k in range(5):
    myOddList.append(y)
    y = y + 2
    
print(myOddList)    

myList = [1,2,3,4,7,9]
newList = []

for i in myList:
    newList.append(i*i)

print(newList)

#Using comprehension:
comList = [i*i for i in myList if i%2 == 1]

print(comList)
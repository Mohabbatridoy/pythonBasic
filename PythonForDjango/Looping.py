# for i in tuple, range, dictionary, list:
# mytuple = ("a","b","c","d")
# for i in mytuple:
#     print(i)
#
# myList = [('a',1,"bdt"),('b',2,'USd'),('c',3,'cad')]
# for i,j,k in myList:
#     print(f"{i}: {j}: {k}")


# myDict = {
#     'name': "Mohabbat",
#     'age': 22,
#     'country': "Bangladesh"
# }
#
# for key, value in myDict.items():
#     print(f"{key}: {value}")

# for i in range(0,11,2):
#     print(i)

# myList = ['spain','Bangladesh','Dhaka','noyakhali']
# for i in range(len(myList)):
#     print(f"country or city name: {myList[i]}")

###=> more looping technique:
myList = ["apple","orange","apple","pear","banana"]
myList2 = [1,2,3,4,5]
myList3 = ['ad','bd']
# for i, fruit in enumerate(myList):
#     print(f"{i} index of {fruit}")
#     print(i)

for i , j in zip(myList2, myList):
    print(i,j)

for i in sorted(myList):
    print(i)
print("\n***********************\n")
for i in reversed(sorted(myList)):
    print(i)
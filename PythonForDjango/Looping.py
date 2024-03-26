# for i in tuple, range, dictionary, list:
# mytuple = ("a","b","c","d")
# for i in mytuple:
#     print(i)
#
# myList = [('a',1,"bdt"),('b',2,'USd'),('c',3,'cad')]
# for i,j,k in myList:
#     print(f"{i}: {j}: {k}")


myDict = {
    'name': "Mohabbat",
    'age': 22,
    'country': "Bangladesh"
}

for key, value in myDict.items():
    print(f"{key}: {value}")

#comprehension:
#iterable : List, tuple, dictionary, set , range:
# create => list, dictionary, set

##=> creating list,dictionary, set, Tuple from list:
# myList = [1,2,3,4,5,6]
# newList = [i+1 for i in myList]
# newDict = {i-1: i*i for i in myList}
# newSet = {i**3 for i in myList}
# newTuple = tuple(i**4 for i in myList)
# newTList = [(i*i, i**3, i**4) for i in myList]
#
# print(newTList)
# print(newTuple)
# print(newSet)
# print(newDict)
# print(newList)

##=> From dictionary to dictionary, set , List, Tuple:
mydict = {
    'name': 'Mohabbat',
    'id': '213-15-4508',
    'age': 22,
    'dob': '25-11-24'
}

newdict = {key +' key': value for key, value in mydict.items()}
newset = {value for i, value in mydict.items()}
newList = [i for i,j in mydict.items()]
newTuple = tuple(i for j,i in mydict.items())
newTList = [(key,value) for key,value in mydict.items()]
print(newTList)
print(newTuple)
print(newList)
print(newset)
print(newdict)
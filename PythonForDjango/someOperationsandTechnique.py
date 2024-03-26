# ##common sequence operatiion:
# #List, Tuple, range
# #List -> mutable/ changeable
# #Tuple -> Immutable /unchangeable
# myTuple = ("Mohabbat", "Bohubrihi",24)
# myTuple2 = ("LOve Rasul(s)",)
# myList = ["Mohabbat","Bohubrihi",22]
# myList2 = ["Love Rasul(s)"]
# myRange = (0,50)
# print("Mohabbat" not in myTuple)
# result = myList + myList2
# print(len(myList))
# print(myList.count('Mohabbat'))
# print(result)

##=> Sequence unpacking :
myTuple = ("Mohabbat", "Bohubrihi",24,[1,2,3])

c1,c2,c3,[c4,c5,c6] = myTuple
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)

myList = ["Mohabbat","Bohubrihi",22]
d1,*d2= myList
print(d1)
print(d2)
# print(d3)

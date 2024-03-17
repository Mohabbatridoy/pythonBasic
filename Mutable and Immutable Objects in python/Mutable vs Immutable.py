# # myStirng = "hello world"
# # print(type(myStirng))
# # print(id(myStirng))
#
# ### Integer Mutable: cause it change the memory location of variable and we can change the variable value:
# numbre = 3
# print(id(numbre))
# numbre = 45
# print(id(numbre))
#
# ## String is immutable:
# # myString = "Hello"
# # print(myString[1])
# # myString[1] = 4
# # print(myString[1])
#
# ## List is mutable:
# myList = [1,2,34,5]
# print(myList[1])
# myList[1] = 3
# print(myList)
#
# ##Tuple is immutable:
# myTuple = (1,2,31,4)
# print(myTuple[1])
# myTuple[1] = 3
# print(myTuple)

myTuple = (1,[2,3,4,5],6,7,8)
print(myTuple)
myTuple[1][1] = 4
print(myTuple)

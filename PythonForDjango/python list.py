myList = ["Bhutan","Nepal","France","Italy","algeria","Brazil",
          "Germany"]
#
# print(myList[-1])
#
# #slicing:
# newList = myList[-5:5:2]
# print(newList)

###List methods:
# myList.append("Bangladesh")
# myList.extend(["canada","Lithuiniya","belgium","Denmark"])
# myList.insert(3,"Bangladesh")
#
# myList.remove("France")
# myList.pop(6)
# country = myList.pop()
# myList.clear()
# print(myList)
# print(country)

##Sorting List:
print(myList)
# myList.sort()
# myList.reverse()
myList.sort(key=str.lower,reverse=True)
print(myList)



# str = "Mohabbat"
#
# nstr = str[::]
# print(nstr)
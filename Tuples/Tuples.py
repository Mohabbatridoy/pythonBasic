# sports = ("football","cricket","badminton")
# print(sports[-1])
#
# #Updating Tuple:
# sports = list(sports)
# print(sports)
# sports[1] = "Ha du du"
# sports.append("hoki")
# sports.append("cricket")
# sports = tuple(sports)
# print(sports)
# print(type(sports))

##Looping on tuple:
# fruits = ("Mango","Orange","Kiwi","apple")
# # for i in fruits:
# #     print(i)
# # print("****separator****")
# # for i in range(0, len(fruits)):
# #     print(fruits[i])
#
# i = 0
# n = len(fruits)
# while i <= n:
#     print(fruits[i])
#     i += 1

###Joining two tuple:
number1 = (1,2,3,4,5,7)
numbr2 = (23,22,35,3)
numbers = number1 + numbr2
number1 = list(number1)
numbr2 = list(numbr2)
print(number1, numbr2)
string = ["hmr","mhk"]
numbers = number1 + numbr2 + string
print(numbers)
print(type(numbers))

#=> List is Mutable and Tuple is Immutable and set support tuple
#But set doesn't support list cause list is mutable.



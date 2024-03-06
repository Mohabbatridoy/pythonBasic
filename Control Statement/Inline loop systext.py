# list = []
# i = 1
# while i <=100:
#     list.append(i)
#     i += 1
# print(list)
#
#
# ## Using Inline Loop:
# antoherList = [i for i in range(1,100)]
# print(antoherList)


# Example of inline loop
evenNumberList = [i for i in range(1,100) if i%2 == 0]
print(evenNumberList)
numbers = [2,14,5,32,28,3,7,11,13,15]
oddList = [i for i in  numbers if i%2!=0]
print(oddList)
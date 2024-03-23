# Duplicate value will execute one time,
#sorting is not allowed in set

# mySet = {"mhr","false",1,True}
# print(mySet)
# # mySet = set()
# # print(mySet)
#
# set1 = set("abcdefg")
# print(set1)
# set2 = set("highklmnopqrst")
# print(set2)

#some operation on set
set1 = set("abcdefg")
set2 = set("highklmnopqrst")
# intersection:
print(set1 & set2)

#Union (or):
print(set1 | set2)

#substract:
# print(set1 - set2)
# print(set2 - set1)

# but not operator ^:
print(set1 ^ set2)
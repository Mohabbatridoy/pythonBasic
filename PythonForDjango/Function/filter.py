def func(n):
    return n%2 == 1
l = [1,2,3,4,4,5,3,3,7,8,9]
newlist = list(filter(lambda n: n%2==1,l))
print(newlist)

##=> Reduce function:
from functools import reduce
li = [1,2,3,4,6]
def funct(n,m):
    return n+m
sum = reduce(funct,li)
print(sum)
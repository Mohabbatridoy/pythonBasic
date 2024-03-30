def func (n):
    return n*n*n

l = [2,4,3,1,5]
newList = list(map(func,l))
print(newList)

newset = set(map(lambda n: n*n*n,l))
print(newset)

newdict = tuple(map(lambda n:n*n*n,l))
print(newdict)
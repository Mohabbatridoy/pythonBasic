# mylist = [letter.upper() for letter in 'bohubrihi']
# print(mylist)

##=> Nested loop:
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)

print(matrix)

#comprehension:
myMatrix = [[j for j in range(4)] for i in range(3)]
print(myMatrix)


flatList = [i[0] for i in myMatrix]
print(flatList)
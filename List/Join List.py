numbers = [1,2,3,4,5]
numbersAnother = [10,20,30,40,50]

mergedList = numbers + numbersAnother
print(mergedList)

#Join list using extend() method:

fruits = ["mango","banana","apple"]
othersFruits = ["pinapple","guava"]
fruits.extend((othersFruits))
print(fruits)
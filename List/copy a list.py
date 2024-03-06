numbers = [10,20,40,30,50]
copyOfNumbers = numbers.copy()
print(copyOfNumbers)

#copy list using LIst(iterable) function:
anotherCopyOfNumbers = list(numbers)
print(anotherCopyOfNumbers)

#Using slice:
copyUsingSlice = numbers[:]
print(copyUsingSlice)
print(numbers)
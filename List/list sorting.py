numbers = [4,2,5,6,7,8,3,1]
fruits = ["mango", "banana","apple"]

#using sort() method to sort:
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)


##sorted() method sort a list and create an anoter list
n = [1,2,4,10,100,5,7,6]
sorted_numbers= sorted(n);
print(f"print after using sorted {sorted_numbers}")
print(f"the real numbers = {n}")

sorted_numbers_dec = sorted(n,reverse=True)
print(f"decending order sorted: {sorted_numbers_dec}")

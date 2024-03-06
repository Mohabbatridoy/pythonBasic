car_models = ["bmw","toyota", "audi"]
countries = ["Bangladesh","India","USA"]

print(countries[-1])

countries[-1] = "Russia"

####del method to delete index value
# print(countries)
#
# del countries[1]
# print(countries)


##pop() method to delete index item:

remove_item = countries.pop()
print(countries)
print(f"the removed item is -{remove_item}")

##remove() :
vowels = ['a','e','i','o','u'];
remove_a = vowels.remove('a')
print(vowels)
print(f"successfully removoed {remove_a}")
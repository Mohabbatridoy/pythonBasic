#Recursion is concept that call itself:
# def my_func(n):
#     if n>10:
#         return
#     print(n)
#     my_func(n+1)
#     print(n)
# my_func(1)

## Example with Factorial:
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
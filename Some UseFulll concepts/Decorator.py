##Example with Wrapper function:
# def myFunc():
#     print("hello world")
#
# def print_func(fn):
#     fn
#     print("this is from print function")
#
# print_func(myFunc())
#
# def greet(name):
#     def hello():
#         print("hello I am "+name)
#     return hello
# v = greet("mohabbat")
# v()


# def greet(func):
#     def inner():
#         func()
#         print("I am from greet inner funtion")
#     return inner
# @greet
# def hello():
#     print("Hello I am from hello")
#
# hello()

# zero division error handle by decorator:

def zero_division_handle(func):
    def inner(a,b):
        if b == 0:
            return "Cannot divide by 0"
        return func(a,b)
    return inner

@zero_division_handle
def division (a,b):
    return a/b

print(division(5,3))
print(division(3,0))
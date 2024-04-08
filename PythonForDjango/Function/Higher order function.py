# def hof(fn):
#     print(fn.__name__)
#     fn()
#
# def great():
#     print("Hello world")
# def hello():
#     print("hello Bohubrihi")


# hof(hello)


# li = [1,2,3,4,5,6,7,8,99]
#
# def myFilter(fn,l):
#     newL = []
#     for i in l:
#         if fn(i):
#             newL.append(i)
#     return newL
#
# newList = myFilter(lambda x: x%2==1, li)
# print(newList)

##=> Wrapper function and Decorators:
# def myFunc():
#     def hello():
#         print("Hello world")
#     return hello
#
# f = myFunc()
# f()

def myWrapper(fn):
    def test():
        print("this text is need to add before")
        fn()
        print("this text is need to add after")
    return  test()


def hello():
    print("Hello hello hello")
# Hello = myWrapper(hello)
hello()

@myWrapper
def great():
    print("Hello bohubrihi")
great()
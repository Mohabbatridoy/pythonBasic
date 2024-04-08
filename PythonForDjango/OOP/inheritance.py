class a :
    def __init__(self,n):
        self.name = n
    def hello(self):
        print("hello world")
# obj = a('Mohabbat')
# print(obj)
# obj.hello()

class B:
    def __init__(self,job):
        self.job = job
    def hello(self):
        print(f"{self.job}")

class c(B,a):
    pass


obj = c('mohabbat')
# print(dir(obj))
obj.hello()
print(c.__mro__)


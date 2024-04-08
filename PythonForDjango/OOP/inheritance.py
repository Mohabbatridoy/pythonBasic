class a :
    def __init__(self,n):
        self.name = n
    def hello(self):
        print("hello world")
# obj = a('Mohabbat')
# print(obj)
# obj.hello()

class B(a):
    def __init__(self,name,job):
        super().__init__(name)
        self.job = job
    def hello(self):
        print(f"{self.name} is a {self.job}")


obj = B('mohabbat','student')
obj.hello()

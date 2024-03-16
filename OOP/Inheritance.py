# # Single Inheritance:
#
# class Person:
#     def __init__(self,name,age,):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         return f"My name is {self.name} I am {self.age}" \
#                f" yeat old"
#
# class Student(Person):
#     def __init__(self,name,age,course):
#         self.course = course
#         Person.__init__(self,name,age)
#
# student1 = Student('Mohabbat',22,["c","python"])
# print(student1.introduce())

##Multilevel inheritance: it's somthing like grandFather, Fagher, son:
##Multiple Inheritance: Father Mother is parent class and son is child class:

##Super Function:
class A:
    def __init__(self):
       print("From class A")
class B(A):
    def __init__(self):
       print("From class B")
       super.__init__(self)
class C(B):
    def __init__(self):
        print("From class C")
        super.__init__(self)

class D(C,B):
    def __init__(self):
        print("from class D")
        super.__init__(self)

D = D()

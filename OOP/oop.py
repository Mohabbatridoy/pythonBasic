class Person:
    def __init__(self, name, age , gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print(f"I am {self.name} and i am {self.age} year old, gender {self.gender}")


person1 = Person("mohabbat",21,"male")
person2 = Person("mhr",22,"male")
print(person1.introduction())
print(person2.introduction())
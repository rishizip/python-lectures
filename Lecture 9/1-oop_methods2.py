# 1. to delete object properties and keyword
# class Student:
#     def __init__(self, name):
#         self.name = name
    
# s1 = Student("rishizip")
# print(s1.name)
# del s1
# print(s1) # will throw error as s1 is got deleted

# 2. private(like) attributes & methods
# private attributes are meant to used only within class and aren't acessable outside the class
# to define a private attribute we have to add _ and for method we have to use __ before the attribute
# syntax
# _private = "variable"

# class Person:
#     def __init__(self, name, acc_no, acc_pass):
#         self.name = name
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
       
#     def check(self):
#         return self.__acc_pass
    
# acc1 = Person("rishizip", 12345678, "abcdefgh")
# print(acc1.name)
# print(acc1.acc_no)
# print(acc1.check())

# 3. super() -> super method is used to acess mrthods of parent class
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)

# car1 = ToyotaCar("prius", "electric")
# print(car1.type)

# 4. class method -> abound to class & recives the class as an implicit first argument
# here cls pass as first argument and it indicates base class
# class Person:
#     name = "Your Name"

#     @classmethod
#     def ChangeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.ChangeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)
# also change the name in person class

# summary of methods
# i) static methods -> used when we dont want to use any properties of class or other methods
# ii) class methods(cls) -> use when we want use only class attributes and want to change directly on class
# iii) instance methods(self) -> use when we want to use instance property

# property decorator
class Student:
    def __init__(self, chem, phy, math):
        self.chem = chem
        self.phy = phy
        self.math = math

    # def calpercentage(self):
    #     self.percentage = str((self.chem + self.math + self.phy) / 3) + "%"

    @property
    def percentage(self):
        return str((self.chem + self.math + self.phy) / 3) + "%"
        
stu1 = Student(98, 99, 92)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)
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

class Person:
    def __init__(self, name, acc_no, acc_pass):
        self.name = name
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
       
    def check(self):
        return self.__acc_pass
    
acc1 = Person("rishizip", 12345678, "abcdefgh")
print(acc1.name)
print(acc1.acc_no)
print(acc1.check())
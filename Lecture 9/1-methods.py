# 1. to delete object properties and keyword
class Student:
    def __init__(self, name):
        self.name = name
    
s1 = Student("rishizip")
print(s1.name)
del s1
print(s1) # will throw error as s1 is got deleted
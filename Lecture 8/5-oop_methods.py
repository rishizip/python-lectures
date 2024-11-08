# methods in oop
# methods are functions that belongs to oop
# user can also create their own method

# class Student:
#     def __init__(self, name, marks):
#        self.name = name
#        self.marks = marks 
#        print("adding new student in databse....") 

#     def welcome(self): # method
#         print("welcome dear", self.name)
#     def get_marks(self):
#         return self.marks

# s1 = Student("Karan", 97)
# s1.welcome() # calling method
# print(s1.get_marks())

# static method
# methods that dont use the self parameter
# syntax
class Design:
    @staticmethod # decorator
    def college():
        print("ABC College")
    
p1 = Design()
p1.college()

# decorators allows to wrap another function in order to extend the behaviour of the wrapped function, without parmanently modifying it
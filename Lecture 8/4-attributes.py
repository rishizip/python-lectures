# attributes in py
# data store in objects/class is call attributes

# types of attribute
# i) class attrubute -> common attributes among all objects
# ii) instance attribute -> different attributes among all objects, defines with self

class Student:
    college = "ABC College" # class attribute

    def __init__(self, name, marks):
       self.name = name # instance attribute
       self.marks = marks # instance attribute
       print("adding new student in databse....") 

s1 = Student("Karan", 97) # instance attribute
print(s1.name, s1.marks) 

s2 = Student("Arjun", 98) # instance attribute
print(s2.name, s2.marks) 

# object attribute gets higher priority in code
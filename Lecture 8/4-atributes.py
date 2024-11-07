# atributes in py
# data store in objects/class is call attributes

# types of atribute
# i) class atrubute -> common atributes among all objects
# ii) instance attribute -> different atributes among all objects, defines with self

class Student:
    college = "ABC College" # class atribute

    def __init__(self, name, marks):
       self.name = name # instance atribute
       self.marks = marks # instance atribute
       print("adding new student in databse....") 

s1 = Student("Karan", 97) # instance atribute
print(s1.name, s1.marks) 

s2 = Student("Arjun", 98) # instance atribute
print(s2.name, s2.marks) 

# 0bject atribute gets higher priority in code
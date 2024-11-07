# constructor in python
# all casses have function call _init_(), which is always executed when the obj. is being initiated

# syntax
# def __init__(self, parameter)

# a constructor is always called, if we didn't declare a constructor in our code python will create a defualt constructor  for us

class Student:

# i) defult constructors -> only only self
    def __init__(self):
        pass

# ii) parameterized contsructors -> have extra parameter additionaly
    def __init__(self, name, marks): # define constructor
       self.name = name
       self.marks = marks
       print("adding new student in databse....") 
       # constructor will call for all objects each time


s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 98)
print(s2.name, s2.marks)

# if we declare two constructor the parameterized constructor will execute
# Features in Oops
# 3. inheritence
# when one class is derives the properties & methods of another class
# the main class is call parent/base class & derived class is call child/derived class

# types in inheritence
# i) signle level -> 1 base class & 1 dervied class 
# ii) multi-level -> 1 base class & more than 1 derived class which are dervied from derived class
# ii) multiple level -> more than 1 base class and they gets inherit by child class

# example 1 :
# class Car:
#     @staticmethod
#     def start():
#         print("Car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car): # single level inheritance
#     def __init__(self, brand, color):
#         self.brand = brand
    
# class Fortuner(ToyotaCar): # multi-level inheritance
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Disel")
# car1.start()

# example 2 :
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C() # multiple inheritance
print(c1.varA)
print(c1.varB)
print(c1.varC)
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
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C() # multiple inheritance
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)

# 4. polymorphism 
# when the same operator have different meaning according to the context#
# polymorphism of +
# print(1+2)
# print("rishi" + "zip")
# print([1, 2, 3] + [4 , 5 , 6])

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_number(self):
        print(f"{self.real} + {self.img}j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.show_number()

num2 = Complex(4, 6)
num2.show_number()

num3 = num1 + num2
num3.show_number()

num3 = num1 - num2
num3.show_number()
# we can define operator overloading by using dunder function(function who have double underscore on it)
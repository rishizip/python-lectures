# Features in Oops
# iii) inheritence
# when one class is derives the properties & methods of another class
# the main class is call parent/base class & derived class is call child/derived class
class Car:
    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand

class ToyotaCar(Car):
    def __init__(self):
        pass
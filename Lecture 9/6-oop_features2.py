# Features in Oops
# iii) inheritence
# when one class is derives the properties & methods of another class
# the main class is call parent/base class & derived class is call child/derived class

class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def start_car(self):
        Car.start()

    def stop_car(self):
        Car.stop()

car1 = ToyotaCar("Fortuner", "Black")
car2 = ToyotaCar("Prius", "Red")

car1.start_car()
print("Car name is",car1.name,"\nCar color is",car1.color)
car1.stop_car()

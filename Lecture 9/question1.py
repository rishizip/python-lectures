# define a Circle class to create a circle with radius r using the constructor
# i) define Area() method of the class which calculates the area of circle
# ii) define a Perimeter() method of the class which calculates the perimeter of the circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

def main():
    radius = float(input("Enter circle radius: "))
    c1 = Circle(radius)
    print(f"Area: {c1.area():.2f}")
    print(f"Perimeter: {c1.perimeter():.2f}")

if __name__ == "__main__": main()
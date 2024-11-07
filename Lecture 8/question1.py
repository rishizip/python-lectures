# create student class that takes name & marks of 3 subjects as arguments in constructor. then create a method to print average

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            avg = sum/3
        print("Hey", self.name, "your score is", avg)

s1 = Student("Tony Stark", [100, 100, 100])
s1.get_avg()
# create student class that takes name & marks of 3 subjects as arguments in constructor. then create a method to print average

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = sum(self.marks)
        avg = total / 3
        print("Hey", self.name, "your average score is", avg)

name = input("Enter the student's name: ")

marks = []
for i in range(3):
    mark = int(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

s1 = Student(name, marks)
s1.get_avg()

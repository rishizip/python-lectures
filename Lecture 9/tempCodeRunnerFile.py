# define Employee() class with attributes role, depertment & salary. this class also has a showDetails() merhod
# create an Engineer class that inherites properties from Employee & has the additional attributes name and age

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

def showDetails(self):
    print(f"Role: {self.role}")
    print(f"Department: {self.dept}")
    print(f"Salary: {self.salary}")

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

    def showDetails(self):
        super().showDetails()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


    def main():
        name = input("Enter engineer's name: ")
        age = int(input("Enter engineer's age: "))
        engg1 = Engineer(name, age)
        engg1.showDetails()

if __name__ == "__main__": main()

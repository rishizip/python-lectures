# wap to count the number of students with "A" grade in the following tuple
# ("C", "D", "A", "A", "B", "B", "A")
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# store the above values in a list & sort them from "A" to "D"
new_grade = list(grade)
new_grade.sort()
print(new_grade)
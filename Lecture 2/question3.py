# wap to assign grades on the basis of their marks
# imagine this type of grading system 🥶
print("🏅Student Grade System🏅")
mark = int(input("Enter your marks : "))
if (mark > 90):
    print("Grade A")
elif ((mark <= 89) and (mark >= 80)):
    print("Grade B")
elif ((mark <= 79) and (mark >= 69)):
    print("Grade C")
else:
    print("Grade D")
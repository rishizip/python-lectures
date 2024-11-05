# wap to enter marks of 3 subjects from the user and store them in a dictionary start with a empty dict. and add them one by one. use subject name as key
marks = {}
x = int((input("enter physics marks : ")))
marks.update({"phy" : x})

y = int((input("enter chem marks : ")))
marks.update({"chem" : y})

z = int((input("enter math marks : ")))
marks.update({"math" : z})

print(marks)
# wap to fing greatest of 3 number
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))
if ((a > b) and (a > c)):
    print("A is greatest")
elif ((b > a) and (b > c)):
    print("B is grestest")
else:
    print("C is greatest")
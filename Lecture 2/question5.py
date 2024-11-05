# wap to check if the user can drive or not
age = int(input("Enter your age : "))
# I'm creating a nested loop : loop inside a loop
if(age >= 18):
    if(age >= 80):
        print("You can not drive")
    elif(age == 18):
        print("make a driving license than you can drive")
    else:
        print("You can drive")
else:
    print("You can not drive")
# wap to check if a number entered by the user is odd or even
num = int(input("Enter a number: "))

if num == 0:
    print("0 is neither even nor odd")
elif num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
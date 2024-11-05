# wap to check if a list contains palindrome of elements
# palindrome -> like same from fontside and backside (eg : "racecar")
a = list(input("enter sumn to check is that palindrome or not : "))
b = a.copy()
b.reverse()
if (b == a):
    print("item is palindrome")
else:
    print("item is not palindrome")
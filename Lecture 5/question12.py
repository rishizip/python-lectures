# wap to find factorial of first n number (using for)
# n = int(input("enter a number : "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print("factorial =",factorial)

n = int(input("enter a number : "))
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial =",fact)
# recurssion in python

# when a function calls itself repidetly
# def show(n):
#     if (n == 0): # base case
#         return
#     print(n)
#     show(n-1)
#     print("End")
# show(3)
# dont forget to create base case else it will make infine calls

# recurrence relation
# if the relation depends on (n-1) terms of that relation
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(6))
print(fact(4))
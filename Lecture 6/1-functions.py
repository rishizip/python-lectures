# functions in pythoon

# block of statements that perform a specific task
# syntax 
# declaration of function
# def funcn_name(para 1, para 2):
#     do some work
#     return val
# calling ofv a function
# func_name(arg 1, arg 2)

# waf to calculate sum of two numbers 
# def sum(a, b):
#     s = a + b
#     print(s)
#     return s
# sum(2, 3)

# waf to calculate avg of three number
# def avg(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg
# avg(12, 14, 19)

# types in function
# i) built in function -> functions which are already defined in python
# example : print(), len(), type(), range()

# ii) user defined function -> functions which are defined by programmer or user

# default parameters
# assigning a default value to parameter, which is used when no arrgument is passed
def multi(a, b=2):
    print(f"{a} x {b} =",a*b)
    return a*b
multi(1)
# we have to assign default arguments from last; i.e non default arguments follows default arguments
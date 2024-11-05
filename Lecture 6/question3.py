# waf to print the elements of a list in a single line (list is the parameter)
def signle(a):
    for val in a:
       print(val, end=" ")
    return val
b = [19, 20, 21, 22, 23, 24, 2]
signle(b)
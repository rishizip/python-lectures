# waf to print the elements of a list in a single line (list is the parameter)
def single(a):
    for val in a:
        print(val, end=" ")
    print()

a = input("Enter the list elements separated by spaces: ")
b = list(map(int, a.split()))
single(b)

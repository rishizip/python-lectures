# waf to print all elements in a list using recursion
def print_list(a, idx=0):
    if idx == len(a):
        return
    print(a[idx])
    print_list(a, idx + 1)

user_input = input("Enter a list of items separated by spaces: ")
items = user_input.split()
print_list(items)

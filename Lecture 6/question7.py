# warf to print all elements in a list.
# hint : use list and index as parameters
def print_list(a, idx=0):
    if (idx == len(a)):
        return
    print(a[idx])
    print_list(a, idx+1)

fruits = ["mango", "appple", "banana", "litchi", "orange"]
print_list(fruits)
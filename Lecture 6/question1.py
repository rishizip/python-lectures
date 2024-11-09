# waf to print the length of a list (list is the parameter)
def print_len(a):
    print("The length of the list is:", len(a))

a = input("enter numbers : ")
num = list(map(int, a.split()))

print_len(num)

# explanation
# 1. split() Method
# The split() method in Python is used to break a string into a list of substrings based on a delimiter (default is whitespace)
# 2. map() Function
# The map() function in Python applies a given function to each item of an iterable (like a list) and returns a map object (an iterator). We often use it to convert data types or apply a function to each element of a list.
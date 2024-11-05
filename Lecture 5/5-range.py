# range in python
# returns sequence of number, starting from 0 (by default), increases by 1 (by default) and stops before specified number
# syntax
# range(start?, stop, step?)  ? -> optional 
# print(range(5)) # -> this 5 is stopping condition
# for val in range(5):
#     print(val)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# to print even number b/w 1 to 100
# for i in range(2, 101, 2):
#     print("even number is :",i)

# to print od number b/w 1 to 100
for i in range(1, 101, 2):
    print("od number is :",i)
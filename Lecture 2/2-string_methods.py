# basic methods in string

# 1. concatenation : add two string
# a = "hello"
# b = "world"
# print(a+b)
# lets print it b/w space
# new = a + " " + b
# print(new)

# 2. to print length : it counts space also
# print(len(new))

# 3. Indexing : position of string
# we use [] to access a charcter of a string
# indexing start from zero
# string = "This is a string"
# print(string[2])

# 4. slicing : accesing a part of a string
# positive slicing
# syntax -> str[starting_index : ending_index]
# in cutting, ending index is not included
# code = "Hey !! I'm using visual studio code"
# print(code[7:35])
# alternative ways
# print(code[7:]) # -> if we miss the last index python will cosider it as ending indexx, same with starting index
# print(code[7:len(code)])
# print(code[0:6])
# print(code[:6])

# negative slicing
# negative slicing starts with -1 from the ending index
# here also ending index is not count in the time of slicing
name = "apple"
print(name[-4:-1])
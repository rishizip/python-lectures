# some basic operators in py

# Types of operators

# i) Arithmeic Operatos (+, -, /, %, **)
# we are doing basic arithmetic stuff
# % -> to find reminder
# ** -> to find power (eg : 2^2)

# a = 5
# b = 2
# print("a + b :",a + b)
# print("a - b :",a - b)
# print("a * b: ",a * b)
# print("a / b :",a / b)
# print("a % b :",a % b)
# print("a ** b :",a ** b)


# ii) Relational Operator (==, !=, >. <, >=, <=)
# in relational operator we are checking is the condition is true or false
# == -> equal equal to, to compare (eg a == b : we are checking is a is equal to b ?)
# != -> not equal to, to compare (eg a != b : we are checking is a is not equal to b ?)

# a = 15
# b = 20
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)


# iii) Assigment Operators (=, +=, -=, /=, *=, %=, %=, **=)
# in assignment operators we are assign values from right to left side, eg a = 14 : here we assign 14 to a)
# an example of rest opertors

# num = 10
# num = num + 10 
# print(num)
# this will print 20, as num already store 10
# either way we write this code as given below
# num = 10
# num += 10
# print("num :",num)
# it adds and assigns in one line
# rest operants work same


# iv) logical operator (not, and, or)
# this operator return boolean value
# not -> reverse if True then it will return False via vice versa
# and -> if both statements are True then it will return True or it will return False
# or -> if one of the statemend is True then it will return True either False

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print("not a > b :",not(a>b))
print("a > b and a = b :",(a > b) and (a == b ))
print("a < b and a = b :",(a < b) and (a == b ))
print("a < b or a = b :",(a < b) or (a == b ))
print("a > b or a = b :",(a > b) or (a == b ))

# type() -> print type of data
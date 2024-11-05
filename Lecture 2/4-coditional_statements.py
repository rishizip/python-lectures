# coditional statements in python
# i) if, ii) elif, iii) else
# if(condition):    -> if true than this will execute the below statement
#     statement
# elif(condition):   -> if false than this will execute the below statement
#     statement
# else:               -> if all statements are false than below statement will execute
#     statement


# note -> spacing plays a crucial role in python so we have to use 4 space or tab button on before wring the statements
# this thing is call indentation means proper spacing in python
# eg : ->
# if (a = True):
#    print("hello world")

# age = int(input("Enter your age : "))
# if (age >= 18):
#     print("You are adult")
# elif ((age >= 15) and (age <= 17 )):
#     print("You are teeneger")
# else:
#     print("You are kid")

# difference b/w if and elif
# if -> always check the condition
# elif -> only check the condition if if statement is false; only execute if if statement return false

# example 1:
num1 = 5
if (num1 > 2):
    print("greater than 2")
if (num1 > 3):
    print("greater than 3")
    
# example 2
num2 = 5
if (num2 > 2):
    print("greater than 2")
elif (num2 > 3):
    print("greater than 3")
# this code will not print the above elif statement as if statement is true
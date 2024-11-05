# type conversion in python
# rule : only works when the data whoose we want to cast can fit on new data type

# i) type conversion : automatic coversion done by python compiler
# a = 2
# b = 3.28
# sum = a + b
# print(sum)
# this will print 5.29 but a is integer and b is float but python compiler change the value to float
# we can only add float to int or int to float, cant add float to str or vice versa
# logic exist here

# ii) type casting : manual converion done by programmer
# syntax : <data type>(value) -> eg : float(4) -> 4.0
a = int("2") # -> 2 was string before
b = 4.25
print(a + b)

value = 3.14
string = str(value)
print(type(string))
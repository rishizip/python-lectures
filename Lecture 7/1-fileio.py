# file I/o in python
# used to read, write, update a file
f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/demo.txt", "r") # opens a file
data = f.read()
print(data)
print(type(data))
f.close() # closes a file
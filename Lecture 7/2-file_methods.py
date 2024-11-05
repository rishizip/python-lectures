# methods in file I/O
# 1. open a file
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/demo.txt", "r")

# 2. read a file
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/demo.txt", "r")
# data = f.read()
# print(data)
# reads entire file
# f.close()

# i) to get specified no of characters
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/demo.txt", "r")
# data2 = f.read(5)
# print(data2)
# f.close()

# ii) to read a line
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/2-demo.txt", "r")
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# generates an empty \n line space cause at the end of the .txt file there is \n character which cant be seen
# f.close()

# 2. write to a file 
# if we want to write a file which doesn't exist python creates that file for us to write
# i) overwrite a file
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/2-demo.txt", "w")
# f.write("I want learn Javascript tomorrow. After completing python")
# f.close()

# ii) append or update a file
# f = open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/2-demo.txt", "a")
# f.write("\nThen I will move to ReactJS")
# f.close()

# with syntax 
with open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/2-demo.txt", "r") as f:
    data = f.read()
    print(data)
    print(type(data))
# with auto close file
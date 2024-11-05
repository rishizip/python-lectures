# create a new file "practice.txt" using ".py". Add the following data in it
# Hi everyone
# we are learning file I/O
# using Java
# I like programming in Java

# with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing Java\nI like programming in Java")

# waf that replace all occurence of java with python in above file

# def replace_word():
#     with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "r") as f:
#         data = f.read()
#     new_data = data.replace("Java", "Python")
#     print(new_data)
#     with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "w") as f:
#         f.write(new_data)

# replace_word()

# search if the word "learning" exist or not
def check_word():
    word = "learning"
    with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not found")
check_word()
def replace_word():
    with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "w") as f:
    f.write(new_data)
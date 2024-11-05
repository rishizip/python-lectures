# from a file containing no. separeted by comma, print the count of even numbers
count = 0
with open("C:/Users/rishi/Desktop/Python Lectures/Lecture 7/q3-practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)
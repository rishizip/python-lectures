#  waf to find in which line of the file does the word "learning" occur first.
# print-1 if word not found

def check_for_line():
    word = "whatevers"
    data = True
    line_no = 1

    with open(r"C:\Users\rishi\Desktop\Python Lectures\Lecture 7\practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1
print(check_for_line())
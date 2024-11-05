# some basics methods in list

marks = [100, 88.9, 99.91, 88.5, 88.87, 66.25, 77]

# 1. slicing
# positive slicing
# syntax -> str[starting_index : ending_index]
# in cutting, ending index is not included
# print(marks[5 : 6])
# print(marks[2 :])
# print(marks[0:1])
# negative slicing
# negative slicing starts with -1 from the ending index
# here also ending index is not count in the time of slicing
# print(marks[-7:-6])

# 2. append() -> adds a element to the end
# marks.append(66.5)
# print(marks)

# 3. sort() -> sorts a list in ascending order
# marks.sort()
# print(marks)
# reverse sorting -> descending order
# marks.sort(reverse=True)
# print(marks)

# 4. reverse() -> reverse the whole list
# marks.reverse()
# print(marks)

# 5. insert() -> insert element by index
# marks.insert(2, 55.2)
# print(marks)

# 6. remove() -> remove first occurence of the element
# marks.remove(88.5)
# print(marks)

# 7. pop() -> remove a element by index
marks.pop(3)
print(marks)
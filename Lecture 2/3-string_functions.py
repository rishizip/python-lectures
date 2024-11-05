string = "i am coder"

# 1. endswith() -> returns true if the string ends with that substring
# print(string.endswith("r"))
# print(string.endswith("e"))

# 2. capitalize() -> capitalize the 1st character
# only works for 1 time -> it creates a new string and doesn't change the original one
# print(string.capitalize())
# we can do changes also for storing it in orginal string
# string = string.capitalize()
# print(string)

# 3. replace() -> replace all occurences with new value
# string = string.replace("i","We")
# string = string.replace("am","are")
# string = string.replace("coder", "coders")
# print(string)

# 4. find() -> returns 1st index of 1st occurer
# print(string.find("e"))

# 5. count() -> to count occurence of substring
print(string.count("a"))
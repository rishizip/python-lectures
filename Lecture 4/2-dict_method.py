# 1 basic method in dictionary
 
dict = {
    "key" : "value",
    "name" : "Zipfiles",
    "cgpa" : 9.8,
    "marks" : (98, 93, 96),
    "adult" : True,
    "language" : ["eng", "hindi", "japanese"],
}

# 1. keys() -> returns all keys
# print(list(dict.keys()))

#2. values() -> return all values
# print(list(dict.values()))

# 3.items() -> return in pairs(key, value) as turples
# print(dict.items())
# print(list(dict.items()))

# 4. get() -> returns the key according to their value
# print(dict.get("name"))

# 5. update() -> to insert new items
new_dict = {"country" : "India", "eligible" : "Yes"}
dict.update(new_dict)
print(new_dict)

# WHY NEED TWO DIFFERENT METHOD FOR GETTING A VALUE
# print("Processing")
# print(dict.get("name2")) # -> returns None if the key is not a part of the dict
# print("Loding")
# print(dict["name2"]) # -> returns error if the key is not a part of the dict
# print("Excuted")
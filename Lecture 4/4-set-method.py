# basic method in sets

# num = set()

# 1. add() -> to add element; can add only one element per one method
# num.add(1)
# num.add(2)
# num.add(2)
# num.add(5)
# num.add(8)
# num.add(10)
# num.add(13)
# print(num)

#2. remove() -> to remove element
# num.remove(2)
# num.remove(10)
# print(num)

#3. clear() -> empties the set
# print(len(num))
# num.clear()
# print(len(num))

# 4. pop() -> removes random value
# collection = {"college", "coding", "python", "world", "hello", "zipfiles"}
# print(collection.pop())

# 6. union() -> combine both set values and return new
# set1 = {1, 3, 5, 7, 9, 11, 13}
# set2 = {2, 4, 6, 8, 10, 12}
# print(set1.union(set2))
# print(set1)
# print(set2)

# 7. intersection() -> combines common values
set1 = {1, 6, 9, 7, 2, 8}
set2 = {2, 4, 6, 8, 1, 9, 7}
print(set1.intersection(set2))
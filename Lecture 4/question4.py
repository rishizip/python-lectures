# figure out a way how to store 9 & 9.0 as separate values in the set
# you can take help of build in data types

values = {9, 9.0}
print(values)

# lets make 9.0 a string
values1 = {9, "9.0"}
print(values1)

# lets make 9.0 a float
values2 = {
    ("float", 9.0),
    ("int", 9)
}
print(values2)
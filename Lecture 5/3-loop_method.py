# methods in loop
# i) break -> used to terminated the loop when encountered 
# i = 0
# while i <= 10:
#     if (i == 5):
#         i += 1
#         break
#     print(i)
#     i += 1

# ii) continue -> acts as skip (terminate execution in the current iteration and continues from the next iteration)
# to print odd number
# i = 1
# while i <= 10:
#     if (i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# to print even number
# i = 1
# while i <= 10:
#     if (i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1

# iii) pass -> to skip
for i in range(5):
    pass
if i>5:
    pass
print("some useful work")
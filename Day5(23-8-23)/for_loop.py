list_ex = ["Red", "Green", "Yellow"]

for i in list_ex:
    print(i)  # Output: Red Green Yellow

# Nested loop
for i in list_ex:
    for j in i:
        print(j)
    print("\n")  # Output: R e d \n G r e e n \n Y e l l o w \n

# Break
for i in list_ex:
    if i == "Green":
        break
    print(i)  # Output: Red

# Continue
for i in list_ex:
    if i == "Green":
        continue
    print(i)  # Output: Red Yellow

# Range
for i in range(0, 10, 2):
    print(i)  # Output: 0 2 4 6 8

# Else
for i in list_ex:
    print(i)
else:
    print("Done")  # Output: Red Green Yellow \n Done

# When no content
for x in [0, 1, 2]:
    pass

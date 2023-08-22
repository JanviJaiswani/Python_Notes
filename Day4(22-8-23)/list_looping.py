list_ex = ["apple", "banana", "cherry"]
for x in list_ex:
  print(x)

print("\n")

for x in range(len(list_ex)):
    print(list_ex[x])

print("\n")

# while loop
i=0
while i != len(list_ex):
    print(list_ex[i])
    i+=1

print("\n")

# short hand gor loop
[print(x) for x in list_ex]


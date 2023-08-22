print("\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list_ex = []

for x in fruits:
  if "e" in x:
    list_ex.append(x)

print(list_ex)
print("\n")

list2 = [x for x in fruits if "a" in x]

print(list2)
print("\n")

list_ex = [x for x in range(10)]
print(list_ex)
print("\n")

list_ex = [x.upper() for x in fruits]
print(list_ex)
print("\n")

list_ex = ['hello' for x in fruits]
print(list_ex)
print("\n")

list_ex = [x if x != "banana" else "orange" for x in fruits]
print(list_ex)
print("\n")
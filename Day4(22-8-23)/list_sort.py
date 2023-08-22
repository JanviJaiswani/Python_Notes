print("\n")
print("\n")

list1 = ["orange", "kiwi", "banana","mango"]
list1.sort()
print(list1)

#reverse
list1.sort(reverse = True)
print(list1)

#case sensitive
list2 = ["banana", "Orange", "Kiwi", "cherry"]
list2.sort()
print(list2)


list2.sort(key = str.lower)
print(list2)







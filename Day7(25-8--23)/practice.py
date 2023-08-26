words = ["apple", "grape", "watermelon", "orange"]
sorted_by_length = set(sorted(words, key=lambda word: len(word)))
print("Words sorted by length:", sorted_by_length)


list1 = [1, 2, 2, 3, 4, 4, 5]
unilist = list(set(list1))
print("duplicates removed:", unilist)

reversed = set(list1[::-1])
print(reversed)

if 5 in list1: print(list1.index(5))
dict1 = {}
for item,index in enumerate(words):
    dict1[index] = item
    
print(dict1)

list2 = [ ('apple' , 0), ('grape', 1), ('watermelon', 2), ('orange', 3)]
dict2 = dict(list2)
print(dict2)

sum1=0
for i in list1:
    sum1 += i
    
print(sum1)

tuple_list = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
for index, item in tuple_list:
    print(f"Index: {index}, Item: {item}")
    
    
people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 25}]
sort = tuple(sorted(people, key=lambda x: (x['age'], x['name'])))
print("Sorted people:", sort)



length_name = lambda name: len(name)
print(length_name("janvi"))

sq = list(map(lambda x: x**2 , list1))
print(sq)


# list1 = [x**2 for x in range(0,10) if x%2 == 0]
# print(list1)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)  # Output: [1, 3, 5, 7, 9]

# num = [1,2,3]
# x = list(map(lambda x : x**2 ,num))
# print(x)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [num for sublist in nested_list for num in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

set1 = {1,2,3 ,4,5,6}
set2 = {7,4,5,6}
# print(set2.union(set1))
print(set2.difference(set1))

str1 ="a b"
print(str1.split())

numbers = [1, 2, 3, 4, 5]
are_all_positive = all(num > 0 for num in numbers)
print(are_all_positive)


numbers = [1, 2, 3, 4]
pairs = [(x, y) for x in numbers for y in numbers]
print(pairs)

name ="janvi jaiswani"
name1 = [letter.upper() for letter in name if letter == "j" ]
print(name1)

name ="janvi jaiswani"
name1 = {letter: name.count(letter) for letter in name}
print(name1)





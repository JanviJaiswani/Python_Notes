# Creating a tuple
my_tuple = (1, 2, 3, "apple", "banana", "cherry")
print("\n")

# Accessing elements
print( my_tuple[0])      # Accessing the first element
print(my_tuple[-1])      # Accessing the last element
print("\n")

# Slicing
print("Slice:", my_tuple[2:5])  # Slicing from index 2 to 4 (5-1)
print("\n")

# Length of tuple
print("Length:", len(my_tuple))  # Length of the tuple
print("\n")

# Type of tuple
print("Type:", type(my_tuple))  # Type of the tuple
print("\n")

# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated = tuple1 + tuple2
print("Concatenation:", concatenated)
print("\n")

# Replicating tuples
replicated = tuple1 * 3
print("Replicated", replicated)
print("\n")

# Checking if an element exists in the tuple
print("apple" in my_tuple)
print("\n")

# Iterating through a tuple
for item in my_tuple:
    print(item)
print("\n")

# Nested tuples
nested_tuple = ((1, 2), ("a", "b"), (True, False))
print("Nested tuple:", nested_tuple)
print("\n")

#covert into list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("converted" , thistuple)
print("\n")


#Methods
thistuple = ("apple", "banana", "cherry")
print("count apple ::", thistuple.count("apple"))
print("index of cherry",thistuple.index("cherry"))
print("\n")
print('\n')

my_set = set((2,1))

# Add elements to the set
my_set.add(5)
my_set.add(10)
my_set.add(15)

print(my_set)
print('\n')

print("Size:", len(my_set))  
print('\n')

print("Type:", type(my_set))
print('\n')

# in - Check if an element is in the set
print( 10 in my_set)  
print('\n')

# Concatenate sets
other_set = {20, 25}
concatenated_set = my_set | other_set
print("Concatenated Set:", concatenated_set) 
print('\n') 

# Update set with another set
my_set.update({30, 35})
print("Updated Set:", my_set) 
print('\n')

#union 
my_set.union(other_set) 
print("after union ::", my_set)
print('\n')

# Remove an element from the set
my_set.remove(10)
print("After Removing 10:", my_set) 
print('\n')

my_set.pop() 
print("After pop", my_set) 
print('\n')

# Clear the set
my_set.clear()
print("Cleared Set:", my_set) 
print('\n')

#delete 
del other_set
#print(other_set)





import numpy as np

two_dim_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


two_dim_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# can be accessed using list comprehension
print(two_dim_list[1])
print([row[1] for row in two_dim_list])

# can be accessed using the slicing
print(two_dim_array[1,:])
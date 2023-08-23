# Lambda function to square a number
square1 = lambda x: x * x
print(square1(2))  # Output: 4

# Lambda function inside a function
def calculation(n):
    return lambda x: n * x

multi = calculation(2)
multi1 = calculation(2)

print(multi(3))   # Output: 6
print(multi1(4))  # Output: 8

# Lambda function with multiple arguments
avg = lambda x, y: (x + y) / 2
print(avg(3, 6))  # Output: 4.5

# Lambda function as an argument to another function
def myfunc(func, value):
    return 5 + func(value)

cube = lambda x: x * x * x
print(myfunc(cube, 2))  # Output: 13

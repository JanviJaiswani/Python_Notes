# Defining a function 
def sum(a, b):
    return a + b

# Calling the function 
result = sum(2, 3)  # Output: 5
print(result)

# Defining a function that takes variable number of arguments (tuple)
def name(*fname):
    print(fname[1])

# Calling the function with multiple arguments
first_name = name("Riya", "Peter", "Jon")  # Output: Peter
print(first_name)

# Defining a function with keyword arguments
def student_Data(name, age, city):
    print("name:", name, "age:", age, "City:", city)

# Calling the function with keyword arguments
student_Data(age=27, city="Jaipur", name="Jon")

# Defining a function with a default parameter
def myfunc(city="Unknown"):
    print(city)

# Calling the function with and without an argument
myfunc("Delhi")  # Output: Delhi
myfunc()         # Output: Unknown

# Passing a list to a function
def my_fruits(fruits):
    for i in fruits:
        print(i)

fruits = ["apple", "banana", "cherry"]
my_fruits(fruits)  # Output: apple, banana, cherry

# Using recursion to calculate factorial
def recurfun(n):
    if n <= 1:
        return 1
    return n * recurfun(n - 1)

fact = recurfun(4)
print(fact)  # Output: 24

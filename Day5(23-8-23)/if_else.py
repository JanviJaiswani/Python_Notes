# Taking user input for two values
a = int(input("Enter the first value: "))  #lets take 15
b = int(input("Enter the second value: ")) #lets take 10
print("\n")

# Using if-elif-else to compare the values
if a > b:
    print(a, "greater than", b)  # Output: 15 greater than 10
elif a == b:
    print("Same Type")
else:
    print(a, "less than", b)
print("\n")

# Short Hand if 
if type(a) == type(b):
    print("Both have the same type")  # Output: Both have the same type

# Using short Hand if-else (ternary Operator or conditional expression)
print(a) if a > b else print(b)
# output :: 15

x = 10
y = 20
max_value = x if x > y else y
print(max_value)  # Output: 20

# Using 'pass' to avoid errors 
if x == y:
    pass

#And operator
num1 = 33
num2 = 200
num3 = 30
if num2 > num3 and num2 > num1:
    print(num2, "is the greatest!!")  # Output : 200 is the greatest!!


#  Nested if statement

temp = 32  

if temp > 30:
    print("  hot day!")  # Output:hot day!
    if temp > 35:
        print("stay hydrated.")  # Output:  stay hydrated.
else:
    print(" not too hot .")  # Output: not too hot.

print("Enjoy your day!")  # Output: Enjoy your day!

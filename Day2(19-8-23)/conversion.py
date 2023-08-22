# implicit Conversion
num1 = 25
print(type(num1))

num2 = 225.123
print(type(num2))

# num1 coverted into float
sum = num1+num2

print("sum :: " , sum)
print(type(sum))


# explicit coversion

string_num = '23'
print(type(string_num))

int_num = 25
print(type(int_num))

# new_num = int_num + string_num   #error

new_num = int_num + int(string_num)  #explicit conversion

print(new_num)




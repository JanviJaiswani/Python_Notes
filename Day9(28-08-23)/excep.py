
print("Exception handling")

try:
    num = int(input("Enter a number::"))
    num2 = int(input("Enter a Divisor::"))
    print(num // num2)
except ZeroDivisionError:
    print("Invalid Input!!")
except Exception as e:
    print(e)
else:
    print("Divided")
finally:
    print("This will always work")
    

print("Done!!")
# Output
# Exception handling
# Enter a number::2
# Enter a Divisor::0
# Invalid Input!!      
# This will always work
# Done!!
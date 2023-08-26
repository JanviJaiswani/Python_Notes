num = input("Enter a number::")
f=open("data.txt", 'w')
f.write(num)
f.close()

f= open("data.txt",'r')
print(f.read())
f.close()

f=open('hello.txt')
if f:
    print("successful")
print(f.closed)

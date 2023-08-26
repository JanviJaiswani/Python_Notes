import os
print(os.path.isfile("hello.txt"))

f=open("hello.txt",'a')
f.write("Jaiwani")
f.close()

f=open('hello.txt','rb')
print(f.read())
f.close()

with open("example.txt", mode="r", encoding="utf-8", buffering=1) as file:
    content = file.read()
    print(content)
    
file = open("file.txt", "r")
try:
    content = file.read()
finally:
    file.close()
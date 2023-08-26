

f=open('example.txt','r')
data = f.readlines()
for x in data:
    print(x)
f.close()


f = open('hello.txt','r')
words=0
lines=0
char =0
for line in f:
    lines += 1
    line = line.strip("/n")
    char = len(line)
    list1 = line.split()
    words += len(list1)
    
print(words)
print(lines)
print(char)
    
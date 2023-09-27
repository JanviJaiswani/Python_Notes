list1 = [[1,2,3],[4,5,6],[7,8,9]]

list1[1][2] = 10

for row in list1:
     print(row)
     
     
for row in list1:
    for col in row:
        print(col, end=" ")
    print()
        
        

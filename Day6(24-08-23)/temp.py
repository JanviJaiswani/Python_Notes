# list1 = [1,2,3]

# ans = [(x,x*x) for x in list1]
# print(ans)

# # [(1,1),(2,4),(3,9)]
# newlist = []
# for x in list1:
#     newlist.append((x,x*x))
    
# print(newlist)


def add(x,y,z=0):
    return x+y+z

def add(x,y):
    return x+y


print(add(3,3))
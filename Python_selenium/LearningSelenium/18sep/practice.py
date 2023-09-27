from array import array

tup = ()
li =['jan','frb','march']
for i in li:
    tup += (i,)
    
print(tup)

tup2 = (*li,)
print(tup2)


evenOdd = lambda x : "even" if x%2 == 0 else "odd"

print(evenOdd(6))

arr = array('u','abbc')
for i in arr:
    print(i)
    
str1 ="janviJaiswani"
print(" ".join([x for x in str1]))
print(str1[::-1])
    

ex = [x for x in li if x == "jan"]
print(ex)


li1 = [1,2,3,4,5]

avg = lambda x,y: x+y/2
print(avg(2,4))


print('\n')

mydict = {
  "name": "Riya",
  "age": "23",
  "DOJ": 2009,
  "DOJ": 2020,
  "languages": ["Hindi","English"]
  
}
print(mydict)
print('\n')

print(len(mydict))
print('\n')

#loop
for x, y in mydict.items():
  print(x, y)

print('\n')
  
for x in mydict:
    print(mydict[x])

print('\n')

newdic = mydict.copy()
print("copied:" ,newdic)
print('\n')

dic1 = dict(name = "John", age = 26, country = "India")
print("2nd method of copy",dic1)
print('\n')

#access
print(dic1["name"])
print("access using get:",dic1.get("age"))
print('\n')

#keys
print("keys func::",dic1.keys())
print('\n')

#values
print(dic1.values())
print('\n')

#update
dic1["name"]="Rohan"
print("after Updation::",dic1)
print('\n')

#item
print(dic1.items())
print('\n')

#if key is present
if "country" in dic1:
    print("yes")
    
print('\n')
    
#update
dic1.update({"age": 20})
print(dic1.items())
print('\n')

#add
dic1["last_name"] = "Sharma"
print(dic1)
print('\n')


#pop
dic1.pop("age")
print("after pop::",dic1)
print('\n')

 
dic1.clear()
print("after clear::",dic1)
print('\n')

# #delete
# del dic1["last_name"]
# print(dic1)












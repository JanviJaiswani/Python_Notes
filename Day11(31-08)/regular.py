import re

text = "Mohan is 22, Rohan is 18, Nihal is 42 all from Jaipur"

ages = re.findall(r'\d{1,3}',text)
print(ages)

names = re.findall(r'[A-Z][a-z]*',text)
print(names)

newdic= {}

for i in range(len(names)):
    if i < len(ages):
        newdic[names[i]] = ages[i]
    else:
        break
    
print(newdic)

search = re.search("Mihal",text)
if search:
    print(search.span())
    
    
str = "pen men  hen ten"
result = re.findall('[pht]en',str)

for i in result:
    print(i)
    
substi = re.compile('Nihal')
Mihal = substi.sub("Mihal", text)
print(Mihal)

txt = "The8rain9in7Spain"
x = re.split("\d", txt)
print(x)
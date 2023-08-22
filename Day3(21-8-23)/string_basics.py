first_name = "Janvi"
sec_name = "Jaiswani"


print( first_name + " " + sec_name)

#indexing
print(first_name[2])
print(first_name[4])

#multiple lines in string
address = '''Janvi Jaiswani 
521B Thakur Narayan Singh Marg,
Rajapark Jaipur 302004,
Rajasthan.
'''        
print(address)

#quotes
ex = 'Rahul said ,"you are smart!!"'
print(ex)

#looping
for i in first_name:
    print(i)
 
print('\n')   
for i in range(5):
    print(first_name[i])
    

#format
name="Jon"
age=25
location="Jaipur"

example = "My name is {} , I am {} , I live in {}"
print(example.format(name,age,location))
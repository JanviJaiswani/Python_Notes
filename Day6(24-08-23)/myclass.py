class Employee:
    
    name ="Jon"
    age = 20
    
    def __init__(self, name , age):
        self.name = name
        self.age = age
    
    def info(self):
        print("Hey I am {} age {}".format(self.name,self.age))
        

obj1 = Employee("Janvi",22)

print(obj1.info())  # output :Hey I am Janvi age 22
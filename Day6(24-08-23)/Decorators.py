class Employee:
    
    def __init__(self, name , age):
        self._name = name
        self._age = age
    
    def info(self):
        print("Hey I am {} age {}".format(self._name,self._age))
      
    
         
    @property   
    def twice_age(self):
        return 2* self._age
    
    @twice_age.setter
    def twice_age(self ,a):
        self._age =a/2

obj1 = Employee("Janvi",22)

print(obj1.info())
print(obj1.twice_age)
obj1.twice_age = 33
print(obj1.twice_age)

class Person:
    __name = "Person"  # Class-level private variable (not an instance attribute)
    _age = 20  # Class-level protected variable (not an instance attribute)
    salary = 200000  # Class-level public variable
    
    def __init__(self, name, age, salary):
        self.__name = name  # Private instance attribute
        self._age = age  # Protected instance attribute
        self.salary = salary  # Public instance attribute
        
    def display(self):
        print(f"My name is {self.__name} and age is {self._age}")
        
class Worker(Person):
      
    def __init__(self, name, age, salary, city):
        super().__init__(name, age, salary)  # Call the parent class constructor
        self.city = city  # Public instance attribute
        
    def display_work(self):
        print(f"My age is {self._age} and location is {self.city}")
        

# Create a Person instance
per1 = Person("Mohit", 25, 300000)
per1.display()  # Display person's details
print(per1.salary)  # Access person's salary

# Create a Worker instance
worker_instance = Worker("Mohit", 25, 300000, "Kota")
worker_instance.display_work()  # Display worker's details

# Expected Output:
# My name is Mohit and age is 25
# 300000
# My age is 25 and location is Kota

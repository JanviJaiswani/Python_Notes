class Employee:
    employee_count = 0  # Class variable
    
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1 # Incrementing the class variable
        print("{} is the {} Employee!!".format(self.name,self.employee_count))
    
# Creating instances of Employee class
employee1 = Employee("Rohan")   #Rohan is the 1 Employee!!
employee2 = Employee("Preet")   #Preet is the 2 Employee!!
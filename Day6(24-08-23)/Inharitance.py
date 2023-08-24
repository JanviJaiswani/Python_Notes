# Superclass (Parent Class)
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    

# Subclass (Child Class) 
class Manager(Employee):
    def __init__(self, name, employee_id, bonus):
        super().__init__(name, employee_id)
        self.bonus = bonus
    
    def calculate_salary(self):
        base_salary = 30000
        total_salary = base_salary + self.bonus
        return total_salary
    
    def show(self):
        print("{} {}".format(self.name , self.calculate_salary()))


# Creating instances of the subclasses
manager = Manager("Rohan", 101, 10000)
manager.show() #output : Rohan 40000
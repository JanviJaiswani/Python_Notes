class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f" instance with value: {self.value}"
    
    def __repr__(self):
        return f"Example({self.value})"
    
    def __len__(self):
        return len(self.value)
    
    def __add__(self, other):
        return MyClass(self.value + other.value) 
    
obj1 = MyClass([2000,3000])
obj2 = MyClass([3000,3000])

print(str(obj1))       # output:: instance with value: [2000, 3000]
print(obj1 + obj2) 
# output:: instance with value: [2000, 3000, 3000, 3000]
print(len(obj1))
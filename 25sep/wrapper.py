def decorator(cls):
      
    class Wrapper:
          
        def __init__(self, x):
            self.wrap = cls(x)
              
        def get_name(self):
            # fetches the name attribute
            return "Student name is : {}".format(self.wrap.name)
        
        def get_name_upper(self):
            return self.wrap.name.upper()
          
    return Wrapper
  
# @decorator
class student:
    def __init__(self, y):
        self.name = y
  
# its equivalent to saying
# student = decorator(student)
x = student("Janvi")
print(x.get_name()) 
print(x.get_name_upper())
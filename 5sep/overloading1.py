class calc:
    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c):
        return a+b+c

c = calc()
print(c.add(2,3,5))
c.add(2,3)

# can achieve using default arguments

class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

calc = Calculator()
result1 = calc.add(1, 2)       # Calls the first part of the add method
result2 = calc.add(1, 2, 3)    # Calls the second part of the add method




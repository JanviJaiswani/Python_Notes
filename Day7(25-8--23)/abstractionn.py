from abc import ABC , abstractmethod

class Shape(ABC):
    
    def shape_Display(self):
        return "{}".format(self.name)
    
    @abstractmethod
    def area(self):
        pass
    
class Square(Shape):
     
    def __init__(self ,side):
        super().__init__()
        self.side = side
        self.name = "Square"
    

        
    def area(self):
        return self.side*self.side
    

sq = Square(5)
print(sq.area())   #output :25

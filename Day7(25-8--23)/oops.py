class compony:
    
    compony_name = "Apple"
    year =2000
    
    def __init__(self,name,year):
        self.compony_name = name
        self.year = year
    
    @classmethod
    def from_str(cls,str1):
        compony_name,year = str1.split("-")
        return cls(compony_name,year)
        
    
com1 = compony.from_str("Tesla-2005")
print(com1.compony_name)
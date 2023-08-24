class compony:
    
    compony_name = "Apple"
    
    
    def show(self):
        print("Name: {}".format(self.compony_name))
     
    @classmethod
    def cangeName(cls,new_name):
        cls.compony_name= new_name
        
        
emp1 = compony()
emp1.show()   #output : Name: Apple
emp1.compony_name = "Tesla"
emp1.show()    #output : Name: Tesla
print(compony.compony_name)  #output : Apple
compony.cangeName("Tesla")
print(compony.compony_name) #output : Tesla






from threading import Thread

class Myclass(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.temp = None
        
    def run(self):
        for i in range(5):
            print("Hello")
        self.temp = 5+10
            
            
t1 = Myclass()
t1.start()
t1.join()
print(t1.temp)
    
    

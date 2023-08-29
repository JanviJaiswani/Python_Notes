from threading import Thread,current_thread
import time

def display(n):
    print(current_thread())
    for i in range(5):
        print("hey this is threading!!!")
        
t1 = Thread(target=display,args=(5,))
t1.start()

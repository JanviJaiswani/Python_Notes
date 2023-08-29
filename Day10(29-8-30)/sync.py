from threading import *
from time import sleep

myLock = Lock()

def task(myLock , msg):
    myLock.acquire()
    for i in range(5):
        print(msg)
    sleep(3)
    myLock.release()

t1=Thread(target=task,args=(myLock,"Hello",))
t2=Thread(target=task,args=(myLock,"Welcome",))
t1.start()
t2.start()
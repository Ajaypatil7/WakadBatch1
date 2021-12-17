import threading
import time
start=time.time()
def func1():
    for i in range(1,6):
        print("Thread 1 is executing")
        time.sleep(3)
def func2():
    for j in range(1,6):
        print("Thread 2 is executing")
        time.sleep(1)
t1= threading.Thread(target=func1, name="func1")
t2=threading.Thread(target=func2,name="func2")
t1.start()
t2.start()
t1.join()
t2.join()
# func1()
# func2()
end=time.time()
print(end-start)
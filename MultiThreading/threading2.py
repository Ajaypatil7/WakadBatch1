import time
import threading
start=time.time()
sqr=[]
cb=[]
def square():
    for i in range(1,7):
        print(i*i, "Square")
        sqr.append(i*i)
        time.sleep(2)

def cube():
    for j in range(1,7):
        print(j*j*j,"cube")
        cb.append(j*j*j)
        time.sleep(2)
t1=threading.Thread(target=square, name="Square")
t2=threading.Thread(target=cube, name="cube")
t1.start()
t2.start()
t1.join()
t2.join()
print(sqr)
print(cb)
end=time.time()
print(end-start)
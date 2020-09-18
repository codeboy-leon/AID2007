from threading import Thread,Lock

lock = Lock()

a = 0
b = 0
def fun():
    while True:
        lock.acquire()
        if a!=b:
            print('a=%d,b=%d'%(a,b))
        lock.release()


t = Thread(target=fun)
t.start()
while True:
    lock.acquire()
    a+=1
    b+=1
    lock.release()
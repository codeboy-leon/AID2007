
'''
作业 :  1. 创建两个线程,同时执行
           一个线程打印 A---Z
           一个线程打印 1--52
           要求打印顺序为 12A34B56C...5152Z

           提示: 使用同步互斥方法

        2. 10万以内质数之和,分别记录时间
           单进程
           4个进程
           4个线程 求, 记录时间

        3. 线程创建方法
'''

from threading import Thread,Lock
lock1 = Lock()
lock2 = Lock()
A_Z = [chr(i) for i in range(ord("A"),ord("Z")+1)]
def print_number():
    for i in range(1,53,2):
        if i%2 == 0:
            print(i,end='')
            print(i+1,end='')
            lock2.release()
            lock1.acquire()
t = Thread(target=print_number)
lock2.acquire()
t.start()

for i in A_Z:
    lock2.acquire()
    print(i,end='')
    lock1.release()

t.join()
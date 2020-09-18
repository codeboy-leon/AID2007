from multiprocessing import Process
from time import sleep

def th1():
    sleep(2)
    print('吃饭')
    print('--------')

def th2():
    sleep(2)
    print('睡觉')
    print('--------')

def th3():
    sleep(2)
    print('打豆豆')
    print('--------')

things = [th1,th2,th3]
ps=[]
for th in things:
    p=Process(target=th)
    ps.append(p)
    p.start()
for i in ps:
    i.join()
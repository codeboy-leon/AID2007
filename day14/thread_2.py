'''
多线程示例2
'''
from threading import Thread
from time import sleep

#含有参数的线程函数
def fun(sec,name):
    print('含有参数的线程')
    sleep(sec)
    print('%s 线程执行完毕'%name)



jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={'name':"T%d"%i})
    t.setDaemon(True)           #主线程结束,其他分支线程都结束
    jobs.append(t)
    t.start()


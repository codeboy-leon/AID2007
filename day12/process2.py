'''
进程基础实例2
含有参数的进程函数
'''
from multiprocessing import Process
from time import sleep
#带有参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print('I am %s'%name)
        print('I am working...')


# p = Process(target=worker,args=(2,'Leon'))
# p = Process(target=worker,kwargs={'sec':2,'name':'Leon'})
p = Process(target=worker,args=(2,),kwargs={'name':'Leon'})
p.start()
p.join(3)
print('=====================')
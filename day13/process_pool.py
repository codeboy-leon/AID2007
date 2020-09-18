'''

进程池演示
'''
from multiprocessing import Pool
from time import sleep,ctime
#进程池函数
def worker(msg,sec):
    print(ctime(),'---',msg)
    sleep(sec)

#创建进程池
pool = Pool(4)

#向进程池中添加事件
for i in range(10):
    msg = 'Tedu-%d'%i
    pool.apply_async(worker,args=(msg,2))

sleep(5)
pool.close()
pool.join()

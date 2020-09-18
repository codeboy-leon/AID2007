'''

创建进程基础示例
'''
import multiprocessing
from time import sleep

a=1
#进程的执行函数
def fun():
    print('开始运行一个进程')
    sleep(1)


    print('子进程执行结束了')
    global a
    a=10000
    print(a)

#实例化进程对象
p = multiprocessing.Process(target=fun)
#启动进程  自动执行target绑定的函数,进程诞生
p.start()
#进程阻塞等待进程结束后回收
print('主进程在执行!')
sleep(2)
print('主进程事情干完了!')
p.join()
fun()
print(a)
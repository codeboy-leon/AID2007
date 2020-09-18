'''

创建线程基础示例
'''
import threading

from time import sleep
import os
a = 1
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),'播放：葫芦娃')
    global a
    a = 10000
    print(a)
#实例化线程对象
t = threading.Thread(target=music)
#启动线程
t.start()
for u in range(2):
    sleep(3)
    print(os.getpid(),'播放：中国心')
#回收线程
t.join()
print(a)
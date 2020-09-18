'''
自定义进程类
'''
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__()
    def fun(self):
        print('假装干了件大事')

    def run(self) -> None:
        self.fun()
        print('完事了')

p = MyProcess('thanks')
p.run()

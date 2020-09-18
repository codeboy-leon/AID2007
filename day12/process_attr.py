from multiprocessing import Process
from time import sleep

def fun():
    for i in range(3):
        sleep(2)
        print('...')

p = Process(target=fun,name='tarena')
p.start()

print(p.pid)
print(p.name)

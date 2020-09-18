from multiprocessing import Process
from signal import *
import os
def func():
    for i in range(2):
        print("pid:",os.getpid())

p = Process(target=func)
# signal(SIGCHLD,SIG_IGN)

p.start()
p.join()

while True:
    pass
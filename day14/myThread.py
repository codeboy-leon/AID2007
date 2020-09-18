from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__()  #必须重新加载父类

    #作为线程的执行内容
    def run(self) -> None:
        for i in range(3):
            print('playing %s'%self.song)
            sleep(2)

t = MyThread('凉凉')
t.start() #运行run
t.join()
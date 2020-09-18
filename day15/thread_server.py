from threading import Thread
from socket import *
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST,PORT)

class MyThread(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def run(self) -> None:
        while True:
            self.data = self.connfd.recv(1024)
            if not self.data:
                break
            print(self.data.decode())
            self.connfd.send(b'thanks')
        self.connfd.close()


def main():
    sk = socket()
    sk.bind(ADDR)
    sk.listen(5)
    while True:
        connfd,addr= sk.accept()
        t = MyThread(connfd)
        t.start()

if __name__ == '__main__':
    main()
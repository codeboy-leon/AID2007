'''

基于多进程的tcp网络并发模型

'''
from socket import *
from signal import *
from multiprocessing import Process
import sys
#网络地址
HOST = '0.0.0.0'
PORT = 8848
ADDR = (HOST,PORT)

def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'ok')
    connfd.close()


def main():
    #创建tcp套接字
    sk = socket()
    sk.bind(ADDR)
    sk.listen(5)
    print('listen the port %d'%PORT)
    signal(SIGCHLD,SIG_IGN)  #  处理僵尸进程
    #循环等待客户端连接
    while True:
        try:
            connfid,addr = sk.accept()
            print('Connect from',addr)
        #为连接进来的客户端创建新的进程
        except KeyboardInterrupt:
            sys.exit('服务结束')
        p = Process(target=handle,args=(connfid,))
        p.daemon = True
        p.start()


if __name__ == '__main__':
    main()
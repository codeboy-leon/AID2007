'''
非阻塞IO示例
'''
from socket import *
import time
sockfd = socket()
sockfd.bind(('0.0.0.0',8848))
sockfd.listen()
#设置非阻塞
# sockfd.setblocking(False)
log = open('log.txt','wb')
sockfd.settimeout(3)
while True:
    try:
        print('waiting for connent')
        connfd,addr = sockfd.accept()
        print('connent from ',addr)
    except BlockingIOError as e:
        msg = '%s: %s\n'%(time.ctime(),e)
        log.write(msg.encode())
        log.flush()
        time.sleep(2)
    except timeout as e:
        msg = '%s: %s\n' % (time.ctime(), e)
        log.write(msg.encode())
        log.flush()
        time.sleep(2)
    else:
        # 有客户端连接
        data = connfd.recv(1024)
        print(data.decode())
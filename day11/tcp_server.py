from socket import *
tcp_sk = socket(AF_INET,SOCK_STREAM)

tcp_sk.bind(('0.0.0.0',8848))


#处理客户端连接(阻塞函数)
while True:
    print('Waiting for connect...')
    tcp_sk.listen(5)
    connfd, addr = tcp_sk.accept()
    while True:
        print('connect from:',addr)
        data = connfd.recv(1024)
        if not data or data.decode()=='##':
            break
        print('msg of client:',data.decode())

        connfd.send(b'thanks')
    connfd.close()

tcp_sk.close()
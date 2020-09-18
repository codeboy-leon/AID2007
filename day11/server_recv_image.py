from socket import *
tcp_sk = socket(AF_INET,SOCK_STREAM)

tcp_sk.bind(('0.0.0.0',8849))


#处理客户端连接(阻塞函数)
while True:
    print('Waiting for connect...')
    tcp_sk.listen(5)
    connfd, addr = tcp_sk.accept()
    file = open('../project/三吉彩花.jpg', 'wb')
    while True:
        print('connect from:',addr)
        image = connfd.recv(1024)
        if not image:
            file.close()
            break
        file.write(image)

    connfd.close()

tcp_sk.close()
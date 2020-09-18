from socket import *

tcp_sk = socket(AF_INET,SOCK_STREAM)


tcp_sk.connect(('127.0.0.1',8849))
file = open('../day13/test_pool/三吉彩花.jpg', 'rb')
while True:
    image = file.read(1024)
    if not image:
        file.close()
        break
    tcp_sk.send(image)
tcp_sk.close()

from socket import *

tcp_sk = socket(AF_INET,SOCK_STREAM)

tcp_sk.connect(('127.0.0.1',8889))

#收发消息

while True:
    msg = input(">>:")
    tcp_sk.send(msg.encode())
    if msg=='':
        break
    data = tcp_sk.recv(1024)
    print('From server:',data.decode())
tcp_sk.close()
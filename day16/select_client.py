from socket import *

sockfd = socket()
sockfd.connect(('127.0.0.1',7784))
while True:
    msg = input('>>:')
    sockfd.send(msg.encode())
    data = sockfd.recv(1024)
    print(data.decode())

from socket import *

tcp_sk = socket()
tcp_sk.connect(('127.0.0.1', 8849))
while True:

    msg = input('>>:')
    if not msg:
        break
    tcp_sk.send(msg.encode())
    data = tcp_sk.recv(1024)
    print(data)

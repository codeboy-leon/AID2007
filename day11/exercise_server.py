from socket import *
import time

tcp_sk = socket()

tcp_sk.bind(('0.0.0.0',8849))

while True:
    tcp_sk.listen(5)
    connfd,addr = tcp_sk.accept()

    while True:
        data = connfd.recv(5)
        if not data:
            break
        print(data.decode())
        time.sleep(0.1)
        connfd.send(b'thanks')

    connfd.close()
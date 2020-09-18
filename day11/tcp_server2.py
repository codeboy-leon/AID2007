from socket import *

tcp_sk = socket()
tcp_sk.bind(('0.0.0.0', 14547))
while True:


    tcp_sk.listen(5)
    connfd,addr = tcp_sk.accept()
    data = connfd.recv(1024)
    if not data:
        break
    print(data.decode())
    connfd.send(b'thanks')
connfd.close()
tcp_sk.close()
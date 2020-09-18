from socket import *

tcp_sk = socket()
tcp_sk.bind(('0.0.0.0',8848))

tcp_sk.listen(5)
connfd,addr = tcp_sk.accept()

data = connfd.recv(1024)
print(data.decode())
connfd.send(b'thanks')

connfd.close()
tcp_sk.close()

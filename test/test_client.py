from socket import *

tcp_sk = socket()
tcp_sk.connect(('127.0.0.1',8848))

tcp_sk.send(b'hello')
data = tcp_sk.recv(1024)
print(data.decode())
tcp_sk.close()
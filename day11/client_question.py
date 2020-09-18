from socket import *


while True:
    tcp_client = socket()
    tcp_client.connect(('127.0.0.1', 10011))
    msg = input("我:")
    if not msg:
        break
    tcp_client.send(msg.encode())
    data =tcp_client.recv(1024)
    print('siri:',data.decode())
tcp_client.close()
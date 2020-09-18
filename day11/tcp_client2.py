from socket import *


while True:
    tcp_client = socket()
    tcp_client.connect(('127.0.0.1', 14547))
    msg = input(">>:")
    if not msg:
        break

    tcp_client.send(msg.encode())
    data =tcp_client.recv(1024)
    print(data.decode())
tcp_client.close()
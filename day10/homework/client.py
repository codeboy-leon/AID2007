from socket import *

client_sk = socket(AF_INET,SOCK_DGRAM)

server_addr = ('127.0.0.1',8899)

while True:
    word = input("请输入单词：")
    if not word:
        break
    client_sk.sendto(word.encode(),server_addr)
    data,addr = client_sk.recvfrom(1024)
    print(data.decode())

client_sk.close()
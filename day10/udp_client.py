'''

udp 客户端
重点代码!!!
'''
from socket import *

server_addr = ('127.0.0.1',10086)

udp_sk = socket(AF_INET,SOCK_DGRAM)
#发送后接收,与服务端配合
while True:
    msg = input(">>:")
    udp_sk.sendto(msg.encode(),server_addr)
    if not msg:
        break
    data,addr = udp_sk.recvfrom(1024)
    print("来自服务器消息：",data.decode())
#关闭套接字

udp_sk.close()
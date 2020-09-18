'''

udp套接字服务端程序示例
重点代码
'''
from socket import *
#创建udp套接字

udp_sk = socket(AF_INET,SOCK_DGRAM)
#绑定地址
udp_sk.bind(('0.0.0.0',10086))
#接收消息
while True:
    data,addr = udp_sk.recvfrom(1024)
    # if data.decode()=='':
    #     break
    print("来自客户端消息：",data.decode())
#发送消息
    ser_msg = input('>>:')
    udp_sk.sendto(ser_msg.encode(),addr)


#关闭套接字
udp_sk.close()
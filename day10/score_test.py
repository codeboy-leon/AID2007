'''
 创建套接字示例
'''
import  socket

udp_sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_sk.bind(('176.140.6.230',8888))
udp_sk.listen()

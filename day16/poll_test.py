"""
poll io多路复用方法 示例
"""
from select import *
from socket import *

# 搞几个IO 用于监控
tcp_socket = socket()
tcp_socket.bind(('0.0.0.0',8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open('my.log','a')

# io的文件描述符为键,IO对象为值
map = {}

p = poll()  # 生成对象

# 关注IO 维护字典
map[file.fileno()] = file
map[udp_socket.fileno()] = udp_socket
p.register(file,POLLOUT)
p.register(udp_socket,POLLIN|POLLOUT)

print("对IO进行监控")
events = p.poll()

print("events:",events)
print('map:',map)

p.unregister(file)


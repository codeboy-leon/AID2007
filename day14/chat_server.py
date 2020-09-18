"""
Author: Levi
Email: lvze@tedu.cn
Time : 2020-9-12
Env: Python 3.6
socket and Process exercise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST, PORT)

# 存储用户地址信息 {name : address}
user = {}

# 处理进入聊天室
def do_login(sock,name,addr):
    if name in user or '管理' in name:
        sock.sendto(b"FAIL",addr)
        return
    else:
        sock.sendto(b"OK", addr)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
        user[name] = addr # 加入这个人
        # print(user) # 测试

# 处理聊天
def do_chat(sock,name,content):
    msg = "%s : %s"%(name,content)
    for i in user:
        # 除去本人
        if i != name:
            sock.sendto(msg.encode(),user[i])

# 用户退出
def do_exit(sock,name):
    del user[name] # 删除用户
    msg = "%s 退出了群聊"%name
    # 告知其他人
    for i in user:
        sock.sendto(msg.encode(), user[i])

# 子进程函数
def handle(sock):
    # 循环等待接收请求  (总分处理模式)
    while True:
        # 所有请求都在这接收
        data, addr = sock.recvfrom(1024)
        # 将客户端请你去做简单的分割处理
        tmp = data.decode().split(' ', 2)
        # 根据请求选择功能
        if tmp[0] == "L":
            # tmp--> [L,name]
            do_login(sock, tmp[1], addr)
        elif tmp[0] == 'C':
            # tmp --> [C,name,xxxxxx]
            do_chat(sock, tmp[1], tmp[2])
        elif tmp[0] == 'E':
            # tmp--> [E,name]
            do_exit(sock, tmp[1])

# 框架 启动函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)

    p = Process(target = handle,args=(sock,))
    p.start()

    # 父进程发送管理员消息
    while True:
        content = input("管理员消息:")
        msg = "C 管理员消息 " + content
        # 从父进程发送给了子进程
        sock.sendto(msg.encode(),ADDR)


if __name__ == '__main__':
    main()

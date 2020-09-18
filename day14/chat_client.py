"""
聊天室客户端
"""
from socket import *
from multiprocessing import Process
import sys

# 服务器地址
ADDR = ('124.70.133.135', 8000)


# 进入聊天室
def login(sock):
    while True:
        name = input("请输入姓名:")
        # 发送请求
        msg = "L " + name
        sock.sendto(msg.encode(), ADDR)
        # 等待回复
        data, addr = sock.recvfrom(1024)
        # 根据情况处理
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print("该用户已存在")


# 接收消息
def recv_msg(sock):
    while True:
        # 服务端的所有消息都在这接收
        data, addr = sock.recvfrom(1024 * 10)
        msg = "\n" + data.decode() + "\n发言:"
        print(msg,end='')


# 发送消息
def send_msg(sock, name):
    while True:
        try:
            content = input("发言:")
        except KeyboardInterrupt:
            content = "exit"
        # 输入exit表示退出聊天室
        if content == 'exit':
            msg = "E " + name
            sock.sendto(msg.encode(), ADDR)
            sys.exit("您已退出聊天室")

        msg = "C %s %s" % (name, content)
        sock.sendto(msg.encode(), ADDR)


# 流程控制函数
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('0.0.0.0',55555)) # 保证客户端地址不变

    # 进入聊天室
    name = login(sock)

    # 创建子进程
    p = Process(target=recv_msg, args=(sock,))
    p.daemon = True  # 子进程随父进程退出
    p.start()
    send_msg(sock, name)  # 发送消息


if __name__ == '__main__':
    main()

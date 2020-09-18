'''

基于select方法的IO多路复用并发模型
'''
from socket import *
from select import select
#创建坚挺套接字,作为初始监控对象
sockfd = socket()
sockfd.bind(('0.0.0.0',8848))
sockfd.listen(5)
sockfd.setblocking(False)
#设置关注列表
rlist = [sockfd]  #关注监听套接字
wlist = []
xlist = []
#监控关注的IO
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    #遍历就绪的IO列表,分情况讨论,监听套接字和客户端
    for r in rs:
        if r is sockfd:
            connfd,addr = r.accept()
            print()
            #将连接进来的客户端连接陶吉吉儿子加入关注的IO
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            #某个客户端发送了消息
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.cloes()
                continue
            print(data)
            wlist.append(r)
    for w in wlist:
        w.send(b'ok')
        wlist.remove(w)
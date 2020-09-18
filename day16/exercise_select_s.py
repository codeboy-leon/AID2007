from select import select

from socket import *

sockfd = socket()
sockfd.bind(('0.0.0.0',8849))
sockfd.listen(5)
sockfd.setblocking(False)
rlist = [sockfd]
wlist = []
xlist = []
while True:
    rs,rw,rx = select(rlist,wlist,xlist)
    for r in rs:
        if r is sockfd:
            connfd,addr = r.accept()
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            r.send(b'ok')



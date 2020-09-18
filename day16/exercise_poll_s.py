from select import poll
from socket import *

sk = socket()
sk.bind(('0.0.0.0',7777))
sk.listen(5)
p = poll()
# map = {sk.fileno():sk}
sk.setblocking(False)
map = {}
map[sk.fileno()] = sk
p.register(sk,POLLIN)
while True:
    events = p.poll()
    for fd,event in events:
        if fd == sk.fileno():
            connfd,addr = event.accpet()
            map[connfd.fileno()] = connfd
            p.register(connfd,POLLIN)
            connfd.setblocking(False)
        elif event == POLLIN:
            data = map[fd].recv(1024).decode()
            if not data:
                map[fd].close()
                del map[fd]
                p.unregister(fd)
                continue
            print(data)
            map[fd].send(b'ok')




while True:
    events =
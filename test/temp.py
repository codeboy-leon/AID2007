from socket import *
from select import poll

sk = socket()
sk.bind(('0.0.0.0',8848))
sk.listen(5)

p = poll()
map = {}
map[sk.fileno()] = sk
p.resgiter(sk,POLLIN)
sk.setblocking(False)

# while True:
    events = p.poll()
    for fd,event in events:
        if fd == sk.fileno():
            connfd,addr = map[fd].accept()
            p.resgiter(connfd)
            map[connfd.fileno()] = connfd
        elif event == POLLIN:
            data = map[fd].recv(1024).decode()
            if not data:
                map[fd].close()
                p.unresgiter(map[fd])
                map[fd].remove()
            print(data)

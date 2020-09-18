'''

完成一个类,提供给别人
让他能够用这个类快速的搭建后端web服务

'''


from socket import *
from select import select
import re

class WebServer:
    def __init__(self,host,port,html):
        self.host = host
        self.port = port
        self.html = html
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host,self.port)
        self.sock.bind(self.address)

    def send_info(self,connfd,info,):
        if info == '/':
            filename=self.html+'/index.html'
        else:
            filename = self.html+ info
        try:
            file = open(filename,'rb')
            web = file.read()
        except:
            response = "HTTP/1.1 400 Not Found!!!\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            connfd.send(response.encode() + b'<p>sorry!!</>')
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            connfd.send(response.encode() + web)

    def start(self):
        self.sock.listen()
        self.rlist = [self.sock]
        self.wlist = []
        self.xlist = []
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for item in rs:
                if item is self.sock:
                    connfd,addr = self.sock.accept()
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    self.handle(item)

    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        result = re.match(r"[A-Z]+\s+(?P<info>/\S*)",request)
        if result:
            info = result.group("info")
            print("请求内容:",info)
            self.send_info(connfd,info,)
        else:
            self.rlist.remove(connfd)
            connfd.close()
            return

if __name__ == '__main__':
    httpd = WebServer(host='0.0.0.0',port=8777,html='./static')
    httpd.start()

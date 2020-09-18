
from socket import *
from threading import Thread
import os
from time import sleep
HOST = '0.0.0.0'
PORT = 8899
ADDR = (HOST,PORT)
class FTPserver(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()
    def show_list(self):
        self.filelist = os.listdir('FTP')
        if not self.filelist:
            self.connfd.send(b"FAIL")
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            msg = '\n'.join(self.filelist)
            self.connfd.send(msg.encode())

    def update_file(self,fileName):
        if os.path.exists('FTP/'+fileName):
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            file = open('FBI'+fileName,'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                file.write(data)
            file.close()
    def download_file(self):
        pass
    def run(self) -> None:
        while True:
            self.data = self.connfd.recv(1024).decode()
            if self.data == 'LIST':
                self.show_list()
            elif self.data[:4] == 'STOR':
                fileName = self.data.split(' ')[-1]
                self.update_file(fileName)
            elif self.data == 'REIR':
                pass
            elif self.data == 'EXIT':
                pass
            print(self.data)
            self.connfd.send(b'thanks')
        self.connfd.close()


def main():
    sk_server = socket()
    sk_server.bind(ADDR)
    sk_server.listen(5)
    while True:
        connfd,addr = sk_server.accept()
        t = FTPserver(connfd)
        t.start()

if __name__ == '__main__':
    main()
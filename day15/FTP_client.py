
from socket import *
from threading import Thread
import sys
sk_client = socket()
sk_client.connect(('127.0.0.1',8899))
class FTPclient():
    def __init__(self,sock):
        self.sock = sock
    def do_list(self):
        self.sock.send(b'LIST')
        self.recv = self.sock.recv(1024)
        if self.recv.decode() == 'FAIL':
            print('文件列表为空')
        else:
            self.result = self.sock.recv(1024*1024).decode()
            print(self.result)

    def do_stor(self,filename):
        try:
            self.file = open(filename,'rb')
        except:
            print('文件不存在!')
        self.sock.send(b'STOR ' + filename.encode())
        ret = self.sock.recv(128).decode()
        if ret == 'OK':
            while True:
                self.data = self.file.read(1024)
                if not self.data:
                    self.sock.send(b'##')
                    break
                self.sock.send(self.data)
            self.file.close()
while True:
    print("""
            1 查看文件
            2.上传文件
            3.下载文件
            4.退出系统
    """)
    ftp = FTPclient(sk_client)
    choose = input('请选择:')
    if choose == '1':
        ftp.do_list()
    elif choose == '2':
        file = input("请输入你需要上传的文件:")
        ftp.do_stor(file)
    elif choose == '3':
        sk_client.send(b'REIR')
    elif choose == '4':
        sys.exit()
from socket import *
tcp_sk = socket()
tcp_sk.bind(('0.0.0.0',10011))
question_dict = {'你几岁了':'我2岁了','你是男生女生啊':'我是机器人','今天股票怎么样':'我还小听不懂',
                 'fuck you':'别跟我扯犊子'
                 }
tcp_sk.listen(5)
while True:

    connfd,addr = tcp_sk.accept()
    data = connfd.recv(1024)
    if not data:
        break
    connfd.send(question_dict[data.decode()].encode())
connfd.close()
tcp_sk.close()
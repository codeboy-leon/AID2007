'''
练习 : 将 first.html作为一个要展示的网页
当用户的请求内容是 /first.html的时候则将这个
网页内容作为一个响应体提供给浏览器

如果浏览器请求的是其他内容则 返回一个404的响应,
内容自定

要求浏览器可以循环的访问

思路 : 1 服务端循环模型
      2. 接收到请求后要提取请求内容
      3. 根据请求内容分情况讨论
'''

from socket import *
import re

sk = socket()
sk.bind(('0.0.0.0',8848))
sk.listen(5)
with open('first.html','rb') as file:
    first = file.read()

while True:
    connfd,addr = sk.accept()
    data = connfd.recv(1024).decode()
    ret = re.findall('GET.*/first.html',data)
    if ret:
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        connfd.send(response.encode()+first)
    else:
        response = "HTTP/1.1 400 Not found\r\n"
        connfd.send(response.encode())

from socket import *

sock = socket()
sock.bind(('0.0.0.0',8848))
sock.listen(5)

connfd,addr = sock.accept()
print('connect from ..',addr)
#接受来自浏览器的http请求

data = connfd.recv(1024*10)
print(data.decode())
with open('../project/三吉彩花.jpg', 'rb') as file:
    image = file.read()
response = "HTTP/1.1 200 OK\r\n"
# Conntent-Type:text/html

# <html>
# <head></head>
# <body>
# <p style=color:red>
# this is a test
# </p>
#
# </body>
# </html>

response+="Content-Type:image/jpg\r\n"
response+="\r\n"
response = response.encode()+image
connfd.send(response)

connfd.close()
sock.close()
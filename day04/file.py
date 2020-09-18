import os

print(os.path.getsize("./4.txt"))
print(os.path.getsize("../day03/my.log"))
#查看一个文件夹下的内容
print(os.listdir("."))
print(os.listdir("../day03"))
#判断一个文件是否存在
print(os.path.exists("./4.txt"))
#查看一个文件是否为普通文件
print(os.path.isfile("4.txt")) #文件返回true
print(os.path.isfile("../day03")) #文件夹返回false

#删除文件
os.remove("test.py")
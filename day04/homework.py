import re
file = open("log.txt","r")
data = file.read()
while True:
    ret = input("请输入一个端口的名字:")
    res = re.split("\n{2}",data)
    for item in res:
        if re.findall(ret,item):
            try:
                ip_port = re.search("(\d{1,3}\.){3}\d+.\d+",item).group()
                print(ip_port)
            except:
                print("ip地址未知")
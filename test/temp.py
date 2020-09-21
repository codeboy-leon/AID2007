import re

ip = 'ip:192.168.122.20  ip:154.554.744.44 ip:192.200.355.155 ip:192.168.22.1'


try:
    result = re.findall(r'(([0-2]\d{1,2}\.){3}[0-2]\d{1,2})',ip)
    print(result)
except:
    print('没有匹配到IP地址')
# s = 'GET 12345'
# 
#
# ret = re.match('\w+',s).group()
# print(ret)
# ret = re.match('(\w+) (/d)',s).group()
# print(ret)
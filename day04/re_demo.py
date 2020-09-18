import re
s = "Alex:2000,Sunny:1999"
pattern = r"(?P<name>\w+):(\d+)"
'''
ret = re.finditer(pattern,s)
for item in ret:
    print(item.span()) #获取匹配内容的位置
    print(item.group()) #获取匹配内容
'''
res = re.match(pattern,s)  #只匹配开头,
res02 = re.search(pattern,s) #只匹配一处
print(res.group())
print(res02.group())


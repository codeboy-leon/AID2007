import re
with open('test.txt','r') as words:
    while True:
        word = words.readline()
        if word=='':
            break
        data = re.findall(r'(\w+)\s+(.*)',word.strip())
        print(data)
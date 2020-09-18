import pymysql
import re
db = pymysql.connect(
    host='176.140.6.230',
    port=3306, user='root',
    passwd='123456', db='dict',
    charset='utf8'
)
cur = db.cursor()

count = 0
with open('dict.txt','r') as words:
    while True:
        word = words.readline()
        if word=='':
            break
        data = re.split(' {1,50}',word.strip(),1)
        temp = []
        data = tuple(data)
        temp.append(data)
        if len(temp[0])<2:
            cur.executemany('insert into words(word) values(%s);',temp)
        else:
            print(temp)
            cur.executemany('insert into words(word,mean) values(%s,%s);',temp)
db.commit()
cur.close()
db.close()
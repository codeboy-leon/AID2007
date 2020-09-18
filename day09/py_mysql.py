import  pymysql

db = pymysql.connect(
    host='176.140.6.230',
    port=3306,user='root',
    passwd='123456',db='stu',
    charset='utf8'
)

cur = db.cursor()
data_list = [(12,'阿狸',24,'w',90)]
# data_list = tuple(data_list)
# print(data_list)

cur.executemany('insert into cls values(%s,%s,%s,%s,%s);',data_list)

cur.close()
db.close()
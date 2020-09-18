import pymysql

mysql = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='stu',charset='utf8')
cur = mysql.cursor()

tem = cur.execute('select * from cls;')
print(cur.fetchone())
for item in cur.fetchall():
    print(item)

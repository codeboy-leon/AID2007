from socket import *
import pymysql

class Database:
    def __init__(self):

        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='dict',
            charset='utf8')
        self.cur = self.db.cursor()
    def close(self):
        self.cur.close()
        self.db.cloes()
    def find_word(self,word):
        self.cur.execute('select mean from words where word=%s',[word])
        result = self.cur.fetchone()[0]
        if result:
            return result
        else:
            return 'Not found'
server_sk = socket(AF_INET,SOCK_DGRAM)
server_sk.bind(('0.0.0.0',8899))
search_word = Database()
while True:
    data,addr = server_sk.recvfrom(1024)
    word = data.decode()
    ret = search_word.find_word(word)
    server_sk.sendto(ret.encode(),addr)
search_word.close()


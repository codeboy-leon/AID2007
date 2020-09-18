import time
file = open("my.log","a+")
file.seek(0,0)
while True:
    time.sleep(2)
    data = time.strftime("%Y-%m-%d", time.localtime())+"\n"
    row = len(file.readlines())+1
    file.write(str(row)+data)
    file.flush()
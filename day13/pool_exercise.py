from multiprocessing import Pool
import os
import time

new_dir = os.mkdir('copy_dir')

def copy_file(dir_name,file_name):
    file = open(dir_name+'/'+file_name,'rb')
    new_file = open('copy_dir' + '/' + file_name, 'wb')
    while True:
        data = file.read(1024)
        if not data:
            break
        new_file.write(data)
    file.close()
    new_file.close()

pool = Pool(3)
test_dir = os.listdir('test_pool')
for item in test_dir:
    pool.apply_async(copy_file,args=('test_pool',item))

print("复制完成")
pool.close()
pool.join()
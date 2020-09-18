from multiprocessing import Process
import os
def get_top_part():
    with open('../day13/test_pool/三吉彩花.jpg', 'rb') as file1:
        size = os.path.getsize('../day13/test_pool/三吉彩花.jpg')
        top_part = size/2
        data = file1.read(int(top_part))
        new_file = open('top.jpg','wb')
        new_file.write(data)
        new_file.close()

def get_bottom_part():
    with open('../day13/test_pool/三吉彩花.jpg', 'rb') as file2:
        size = os.path.getsize('../day13/test_pool/三吉彩花.jpg')
        bottom_part = size/2
        file2.seek(int(bottom_part))
        data = file2.read()
        new_file2 = open('bottom.jpg','wb')
        new_file2.write(data)
        new_file2.close()
p = Process(target=get_bottom_part)
p.start()
get_top_part()
p.join()
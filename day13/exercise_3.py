
from multiprocessing import Pool
import os

# 进程池要做的的事件---拷贝文件..

def copy(filename,old_folder,new_folder):

    print(os.path.getsize(filename))
    fr = open(old_folder+'/'+filename,'rb')
    fw = open(new_folder+'/'+filename,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()


# 创建进程池,执行事件
def main():
    # 获取文件列表
    old_folder = input("要拷贝的目录:")
    filelist = os.listdir(old_folder)
    os.mkdir(old_folder+'-备份')
    new_folder = old_folder+'-备份'

    pool = Pool(4) # 创建进程池

    for file in filelist:
        pool.apply_async(func = copy,
                         args=(file,old_folder,new_folder))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()

#
# 练习3: 在练习2的基础上设计
# 如果在拷贝的过程中能够实时的不断打印拷贝进度
# 不断打印已拷贝的百分比
#
# 文件的总大小 = 所有文件大小之和
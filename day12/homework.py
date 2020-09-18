import time
from multiprocessing import Process
def get_time(fucn):
    def warrper(*args):
        start_time = time.time()
        fucn(*args)
        end_time = time.time()
        spend_time = end_time-start_time
        return spend_time
    return warrper
@get_time
def get_sum(start_num,num):
    sum = 0
    for i in range(start_num,num+1):
        count = 0
        c = i//2
        for j in range(2,c+1):
            if i%j==0:
                count+=1
        if count == 2:
            sum+=i
    print('%d以内的质数和为：%d'%(num,sum))
list_args = [1,25001,50001,75001,100001]
list_p = []
for item in range(len(list_args)):
    if item == len(list_args)-1:
        break
    p = Process(target=get_sum,args=(list_args[item],list_args[item+1]))
    p.start()
    list_p.append(p)
for p in list_p:
    p.join()
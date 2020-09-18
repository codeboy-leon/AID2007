from threading import Thread
from time import sleep

list_ticket = ["T%d"%i for i in range(1,501)]

def sell_ticket(win):
    while True:
        if not len(list_ticket):
            break
        sell_out = list_ticket.pop(0)
        print('%s卖出--%s'%(win,sell_out))
        sleep(0.1)
sell_thread = []
for i in range(10):
    t = Thread(target=sell_ticket,args=('w%d'%i,))
    sell_thread.append(t)
    t.start()
for i in sell_thread:
    i.join()
from multiprocessing import Process,Queue

q = Queue()

def request():
    name = 'leon'
    passwd = '123'
    q.put(name)
    q.put(passwd)

def handle():
    name = q.get()
    passwd = q.get()
    print(name)
    print(passwd)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()

p1.join()
p2.join()
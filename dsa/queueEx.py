import queue

#FIFO first in first out
def fifoEx():
    q = queue.Queue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get())
fifoEx()

#LIFO last in first out (stack)
def lifoEx():
    q = queue.LifoQueue()

    for i in range(5):
        q.put(i)

    while not q.empty():
        print(q.get())
lifoEx()        
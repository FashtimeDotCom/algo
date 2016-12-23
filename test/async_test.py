# coding:utf-8

import time
from multiprocessing import Process, Queue

queue = Queue(maxsize=5)


class ProducerConsumer(object):
    def __init__(self, queue):
        self.queue = queue

    def producer(self):
        for item in xrange(50):
            print "=== producer,", item
            self.queue.put(item)
            time.sleep(1)

    def consumer(self, i):
        while True:
            item = self.queue.get()
            print "=== consumer[{i}],".format(i=i), item


class Task(object):
    def run(self, maxsize, pool_num):
        queue = Queue(maxsize=maxsize)
    
        pc = ProducerConsumer(queue)
    
        pr = Process(target=pc.producer, args=())
        pr.start()

        pool = []
        for i in xrange(pool_num):
            pool.append(Process(target=pc.consumer, args=(i,)))
        for p in pool:
            p.start()

if __name__ == "__main__":
    t = Task()
    t.run(5, 3)

#!/usr/bin/python
# -*- coding: UTF-8 -*-


import Queue
import threading
import time

exitFlag = True  # 退出参数


class myThread(threading.Thread):

    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name  # 线程名
        self.q = q  # 内容

    def run(self):

        print "Starting " + self.name  # 开始线程
        process_data(self.name, self.q)  # 将线程名和写入队列的值传到process方法里
        print "Exiting" + self.name


def process_data(threadName, q):
    while exitFlag:  # 当exitFlag为True 开始循环
        queuelock.acquire()  # 线程锁开始，只希望一个线程处理一个任务的放里面
        if not workQueue.empty():
            data = q.get()  # 从队列中获取数据
            queuelock.release()  # 线程锁结束，只希望一个线程处理一个任务的放里面
            print "%s processing %s" % (threadName, data)
        else:
            queuelock.release()
        time.sleep(1)


threadlist = ['Thread-1', 'Thread-2', 'Thread-3']
namelist = ['one', 'Two', 'Three', 'Frour', 'Five']
queuelock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

for tname in threadlist:
    thread = myThread(threadID, tname, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


queuelock.acquire()
for word in namelist:
    workQueue.put(word)
queuelock.release()


#　等待队列清空 如果队列为空 则not判断为假，结束循环，如果队列不为空，not判断为True 则继续执行
while not workQueue.empty():
    pass


exitFlag = 0

for t in threads:
    t.join()
print 'Exiting Main Thread'

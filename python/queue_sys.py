#! /usr/bin/env python

import time, threading
from threading import Thread
from urllib2 import urlopen
from Queue import Queue

class ClosedSystem(object):
    def __init__(self, _n=2):
        self._n = _n
        self._queue = Queue(_n)
        self._threads = list()
    
    def dowork(self):
        url = self._queue.get()
        response = urlopen(url) 
        #when task is done - 200 response spend some thinking time then again send another request
    
        #get the response 
        while 1:
            data = response.read()
            print data
            if not data:
                break
        self._queue.task_done()
 
    # 1. initializes `n` threads
    # 2. initializes the queue with urls
    def setup(self):
        for i in range(self._n):
            t = Thread(target=self.dowork) 
            t.daemon = True 
            self._threads.append(t)
        
        for i in range(self._n):
            self._queue.put('http://localhost:3001')
    
    def start(self):
        for i in range(self._n):
            self._threads[i].start()
        while threading.active_count() > 0:
            time.sleep(1)
def main():
    a = ClosedSystem(10)
    a.setup()
    a.start()

if __name__ == "__main__":
    main()

#! /usr/bin/env python

#from urllib import urlopen

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

class ClosedSystem(object):
    def__init__(self, _n=200):
        self._n = _n
        self._queue = Queue(_n)
        self._threads = list()
    
    def _dowork(self):
        while true:
            url = self._q.get()
            url = __getStatus(url)
            self._q.task_done()

    def __getstatus(self, ourl):
        try:
            url = urlparse(ourl)
            conn = httplib.HTTPConnection(url.netloc)
            conn.request("HEAD", url.path)
            res = conn.getresponse() 
            return res.status
        except:
            return "error", ourl
    
    # 1. initializes `n` threads
    # 2. initializes the queue with urls
    def setup(self):
        for i in range(self._n):
            t = Thread(target=_doWork)
            t.daemon = true
            self._threads.append(t)
        
        for i in range(self._n):
            self._queue.put('http://localhost:3000')
    
    def start(self):
        for i in range(self._n):
            self._threads[i].start()
        
        self._queue.join()

def main():

if __name__ == "__main__":
    main()

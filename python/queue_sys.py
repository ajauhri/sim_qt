#! /usr/bin/env python

import time, threading
from threading import Thread
from urllib2 import urlopen

# base class for all types of systems
class System(object):
    def __init__(self, _n):
        self._n = _n
        self._threads = list()

### OpenSystem ###
class OpenSystem(System):
    def __init__(self, _n=2):
        super(OpenSystem, self).__init__(_n)

    def dowork(self, url):
        response = urlopen(url)
        data = response.read()
        print data
        
    def start(self,url):
        while 1:
            for i in range(self._n):
                t = Thread(target=self.dowork, args=(url,))
                t.daemon = True
                self._threads.append(t)
            for i in range(len(self._threads)):
                self._threads.pop().start()

### ClosedBatchSystem ###
class ClosedBatchSystem(System):
    def __init__(self, _n=2):
        super(ClosedBatchSystem, self).__init__(_n) 

    def dowork(self, url):
        response = urlopen(url)
        while 1:
            data = response.read()
            print data
            if not data:
                break

    def start(self, url):
        while 1:
            for i in range(self._n):
                t = Thread(target=self.dowork, args=(url,))
                t.daemon = True
                self._threads.append(t)

            for i in range(self._n):
                self._threads.pop().start()
           
            # ensures that new set of jobs are sent ONLY when the first batch has been completed
            while threading.active_count() != 1:
                time.sleep(1)
                
            # thinking time begins here
            # Don't need to account for this in a CBS
        
### ClosedInterativeSystems ###
class ClosedInteractiveSystem(System):
    def __init__(self, _n=2):
        super(ClosedInteractiveSystem, self).__init__(_n) 

    def dowork(self, url):
        response = urlopen(url)
        while True:
            data = response.read()
            print data
            if not data:
                break

    def start(self, url):
        while 1:
            for i in range(len(self._threads), self._n):
                t = Thread(target=self.dowork,args=(url,))
                t.daemon = True
                self._threads.append(t)

            for i in range(len(self._threads)):
                self._threads.pop().start()
           
            while threading.active_count() == self._n + 1:
                time.sleep(.1)
                

def main():
    a = ClosedInteractiveSystem(10)
    a.start('http://localhost:3000')

if __name__ == "__main__":
    main()

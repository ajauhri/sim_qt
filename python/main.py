#! /usr/bin/env python

from urllib import urlopen

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

#from schd_policy import sjf, srpt, fsfs
#from queue_sys import closed_sys, open_sys


# this can be done for open systems as response is independent of requests
def make_request():
    for i in range(100): 
        urlopen('http://localhost:3000')

if __name__ == "__main__":
    make_request()

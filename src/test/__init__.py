#encoding: UTF8
import time
import urllib2
import re
import StarchScanner
import StarchScanner.Model
from _io import open

scanner = StarchScanner.scanner
          
scanner.start()
        
def asdf(response, content, code):
    print content

for x in range(1,10):
    scanner.addTask(StarchScanner.Model.HttpTask('http://www.baidu.com/', asdf, True))
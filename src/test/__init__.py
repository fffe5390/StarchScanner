#encoding: UTF8
import os
import time
import urllib
import urllib2
import re
import StarchScanner
import StarchScanner.Model
import random
import threading

scanner = StarchScanner.scanner
mutex = threading.Lock()
scanner.start()
          
def asdf(response, content):
    ConTp = response.info().getheader('Content-Type')
    if 'GBK' in (ConTp if ConTp else ''):
        content = content.decode('GBK').encode('UTF8')
    pattern = re.compile(r'<title>(.*?)</title>')
    results = pattern.finditer(content)
    for res in results:
        print urllib.unquote(response.geturl()), res.group(1)
        mutex.acquire()
        output = open('./results.txt', 'a')
        output .write(urllib.unquote(response.geturl()) +'   ——————————   '+ res.group(1) + '\n')  
        output .close()
        mutex.release()

for x in range(3354324916, 3354314916, -1):
    scanner.addTask(StarchScanner.Model.SimpleHttpTask('http://tieba.baidu.com/p/'+str(x), asdf, True))
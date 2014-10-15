#encoding: UTF8
import time
import urllib2
import re
import StarchScanner
import StarchScanner.Model
import random

scanner = StarchScanner.scanner
          
scanner.start()
        
def asdf(response, content, code):
    pattern = re.compile(r'<h4 class="uname">(.*?)</h4>')
    results = pattern.finditer(content)
    for res in results:
        print response.geturl(),res.group(1)

for x in xrange(54999,56023):
    scanner.addTask(StarchScanner.Model.HttpTask('http://space.bilibili.com/'+str(x), asdf, True))
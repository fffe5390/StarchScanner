#encoding: UTF8
import time
import urllib
import urllib2
import re
import StarchScanner
import StarchScanner.Model
import random

scanner = StarchScanner.scanner
            
scanner.start()
          
def asdf(response, content):
    pattern = re.compile(r'<title>(.*?)</title>')
    results = pattern.finditer(content)
    for res in results:
        print urllib.unquote(response.geturl()), res.group(1).decode('GBK').encode('UTF8')
   
# for x in range(3354118644,3354018644,-1):
#     scanner.addTask(StarchScanner.Model.SimpleHttpTask('http://tieba.baidu.com/p/'+str(x), asdf, True))

scanner.addTask(StarchScanner.Model.SimpleHttpTask('http://tieba.baidu.com/p/3354318644', asdf))
#encoding: UTF8
import urllib2
import gzip
import StringIO
import StarchScanner

#task的基类，只包含需要执行的函数
class Task(object):
    def __init__(self, callback, args):
        super(Task, self).__init__()
        self.callback = callback
        self.args = args




#特化Task，封装了Task，用于http，func函数原型是func(response, content, statecode)，func由用户给出，用于处理接收到的数据
#设计思路：将用户的func函数包装在一个网络访问的函数callback里，然后SimpleHttpTask就可以作为Task对待
class SimpleHttpTask(Task):
    def __init__(self, url, func, proxy=False):
        super(SimpleHttpTask, self).__init__(self._openurl, ())#因为_openurl的参数在本类可获取，所以不需要传进去
        self.url = url
        self.func = func
        self.proxy = proxy
        self.retrycount = StarchScanner.config.HTTPTASKRETRYCOUNT


    #封装func，成为一个具有完整网络访问功并且和处理Scanner内部事务的函数，该函数会被赋值给self.callback，用于在线程中调用
    def _openurl(self):
        
        if self.retrycount <= 0:
            
            print '————————————————————————————'
            print '超出最大重试次数，此任务放弃'
            print 'url:',self.url
            print '————————————————————————————'
            return
        
        request = urllib2.Request(self.url)
        request.add_header('User-Agent', StarchScanner.userAgents.random())
        
        if self.proxy:
            request.set_proxy(StarchScanner.proxies.random(), 'http')
            
        try:
            response = urllib2.urlopen(request, timeout = StarchScanner.config.HTTPTIMEOUT)
            content = response.read()
            
        except urllib2.HTTPError, e:
            print '————————————————————————————'
            print '发生HTTPError，task重入队列'
            print 'url:',self.url
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        except urllib2.URLError, e:
            print '————————————————————————————'
            print '发生URLError，task重入队列'
            print 'url:',self.url
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        except Exception, e:
            print '————————————————————————————'
            print '发生异常，task重入队列'
            print 'url:',self.url
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        ConEncod = response.info().getheader('Content-Encoding')
        if 'gzip' in (ConEncod if ConEncod else ''):
            data = StringIO.StringIO(content)
            gz = gzip.GzipFile(fileobj=data)
            content = gz.read()
            gz.close()
        self.func(response, content)
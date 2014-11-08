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




#特化Task，封装了Task，用于http，func函数原型是func(response, content)，func由用户给出，用于处理接收到的数据
#设计思路：将用户的func函数包装在一个网络访问的函数callback里，然后HttpTask就可以作为Task对待
class HttpTask(Task):
    def __init__(self, request, func, ifproxy=False):
        super(HttpTask, self).__init__(self._request, ())#因为_request的参数在本类可获取，所以不需要传进去
        self.request = request
        self.func = func
        self.ifproxy = ifproxy
        self.retrycount = StarchScanner.config.HTTPTASKRETRYCOUNT


    #封装func，成为一个具有完整网络访问功并且和处理Scanner内部事务的函数，该函数会被赋值给callback，用于在线程中调用
    #参数request为生成的urllib2.Request对象
    def _request(self):
        
        if self.retrycount <= 0:
            
            print '————————————————————————————'
            print '超出最大重试次数，此任务放弃'
            print 'url:',self.request.get_full_url()
            print '————————————————————————————'
            return
        
        self.request.add_header('User-Agent', StarchScanner.userAgents.random())
        
        if self.ifproxy:
            self.request.set_proxy(StarchScanner.proxies.random(), 'http')
            self.request.add_header('Accept-Encoding', 'gzip')
            
        try:
            response = urllib2.urlopen(self.request, timeout = StarchScanner.config.HTTPTIMEOUT)
            content = response.read()
            
        except urllib2.HTTPError, e:
            print '————————————————————————————'
            print '发生HTTPError，task重入队列'
            print 'url:',self.request.get_full_url()
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        except urllib2.URLError, e:
            print '————————————————————————————'
            print '发生URLError，task重入队列'
            print 'url:',self.request.get_full_url()
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        except Exception, e:
            print '————————————————————————————'
            print '发生异常，task重入队列'
            print 'url:',self.request.get_full_url()
            print e
            print '————————————————————————————'
            self.retrycount -= 1
            StarchScanner.scanner.addTask(self)
            return
        
        ConEncod = response.info().getheader('Content-Encoding')
        if 'gzip' in (ConEncod if ConEncod else ''):
            data = StringIO.StringIO(content)
            gz = gzip.GzipFile(fileobj=data)
            try:
                content = gz.read()
            except IOError, e:
                gz.close()
                print '————————————————————————————'
                print '发生gzip解压异常，task重入队列'
                print 'url:',self.request.get_full_url()
                print e
                print '————————————————————————————'
                self.retrycount -= 1
                StarchScanner.scanner.addTask(self)
                return
            
        self.func(response, content)


class SimpleHttpTask(HttpTask):
    def __init__(self, url, func, ifproxy=False):
        super(SimpleHttpTask, self).__init__(urllib2.Request(url), func, ifproxy)
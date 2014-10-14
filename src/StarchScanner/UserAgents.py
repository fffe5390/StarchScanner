#encoding: UTF8
import random

class UserAgents(object):
    def __init__(self):
        super(UserAgents, self).__init__()
        self.userAgents = [
                           'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
                           'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
                           'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                           'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)'
                           'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                           'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                           'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                           'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Version/3.1 Safari/525.13',
                           'Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13',
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6'
                           ]
        
    def random(self):
        return random.choice(self.userAgents)
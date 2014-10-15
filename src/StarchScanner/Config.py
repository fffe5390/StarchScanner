#encoding: UTF8
import os

#生成默认配置类
class Config(object):
    def __init__(self):
        super(Config, self).__init__()
        #主任务队列最大长度
        self.MAXTASKQUEUE = 1000
        
        #线程分发间隔时间，单位秒
        self.THREADINTERVAL = 1
        
        #http等待时间
        self.HTTPTIMEOUT = 10
        
        #代理池文件路径
        self.PROXIESPATH = os.path.dirname(__file__) + "/" + "proxies.txt"
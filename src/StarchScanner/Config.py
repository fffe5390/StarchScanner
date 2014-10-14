#encoding: UTF8

#生成默认配置类
class Config(object):
    def __init__(self):
        super(Config, self).__init__()
        #主任务队列最大长度
        self.MAXTASKQUEUE = 1000
        
        #线程分发间隔时间，单位秒
        self.THREADINTERVAL = 1
        
        #http等待时间
        self.HTTPTIMEOUT = 20
        
        #代理吃文件路径
        self.PROXIESURI = "D:/proxies.txt"
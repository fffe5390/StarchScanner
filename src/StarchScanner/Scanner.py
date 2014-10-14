#encoding: UTF8
import Queue
import util
import time
import StarchScanner

class Scanner(object):
    #初始化
    def __init__(self):
        super(Scanner, self).__init__()
        
        #主任务队列
        self.taskQueue = Queue.Queue(StarchScanner.config.MAXTASKQUEUE)
        
        
        
        
    #启动爬虫
    def start(self):
        
        #启动task消费模块的线程
        util.CreateThread(self._taskCsr, ()).start()
    
    
    #直接添加任务到主队列
    def addTask(self, task, timeout=None):
        self.taskQueue.put(task, True, timeout)
    
    #task消费模块函数
    def _taskCsr(self):
        while True:
            task = self.taskQueue.get()
            util.CreateThread(task.callback, task.args).start()
            time.sleep(StarchScanner.config.THREADINTERVAL)
            
            
        
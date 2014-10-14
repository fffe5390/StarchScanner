#encoding: UTF8
import threading

#根据函数创建线程
class CreateThread(threading.Thread):
    def __init__(self, callback, args):
        super(CreateThread, self).__init__()
        self.callback = callback
        self.args = args
        
    def run(self):
        self.callback(*self.args)
        

#encoding: UTF8
import random
import StarchScanner

class Proxies(object):
    def __init__(self):
        super(Proxies, self).__init__()
        self.proxies = []
        self.loadProxies()
        
    def random(self):
        return random.choice(self.proxies)
    
    def loadProxies(self):
        f = open(StarchScanner.config.PROXIESPATH, 'r')  
        for line in f:  
            self.proxies.append(line)
        f.close()
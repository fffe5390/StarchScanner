#encoding: UTF8
import os
import Scanner
import Proxies
import UserAgents
import Config

#config
config = Config.Config()

#ua池
userAgents = UserAgents.UserAgents()

#代理池
proxies = Proxies.Proxies()

#扫描器
scanner = Scanner.Scanner()
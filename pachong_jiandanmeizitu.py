import urllib.request
import threading,time,random
import re
import queue
from timeit import Timer
import _thread
import os


num1 = input('请输入起始页：')
# print (num1)
num2 = input('请输入终止页：')
web_all = []
webdizhi = []
# print(int(num1),int(num2))
for i in range(int(num1),int(num2)+1):
    # print(i)
    response = urllib.request.urlopen('http://jandan.net/ooxx/page-%d#comments' % i)
    html = response.read()
    html_str = html.decode('utf-8')
    pattern = re.compile('img src="//wx.*.jpg')
    groups = pattern.findall(html_str)
    # print(groups)
    web_all.append(groups)
for i in web_all:
    for j in i:
        webdi = 'http:' + j[9:]
        webdizhi.append(webdi)

q = queue.Queue()
for i in webdizhi:
    q.put(i)

class ThreadDemo(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i = i
        # self.x = x
        # self.y = y
    def run(self):
            pattern  = re.compile('[0-9a-zA-Z]{32}')
            groups = pattern.findall(self.i)
            groups_str = ''.join(groups)
            # print(groups_str)
            urllib.request.urlretrieve(self.i,'c:\\github\pictures\%s.jpg' % groups_str)
            # self.x = self.x + 1
            print('%s 正在下载。。。' % groups_str)
while not q.empty():
    for i in range(4):
        # print(i)
        thread = ThreadDemo(q.get())
        thread.start()
x = raw_input('start')

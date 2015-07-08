#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的Python爬虫, 使用了多线程, 
爬取豆瓣Top前250的所有电影

Anthor: Andrew Liu
Version: 0.0.2
Date: 2014-12-14
Language: Python2.7.8
Editor: Sublime Text2
Operate: 具体操作请看README.md介绍
"""

import urllib2, re, string
import threading, Queue, time
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')
_DATA = ["","","",""]
SHARE_Q = Queue.Queue()  #构造一个不限制大小的的队列
_WORKER_THREAD_NUM = 4  #设置线程的个数

class MyThread(threading.Thread) :

    def __init__(self, func) :
        super(MyThread, self).__init__()  #调用父类的构造函数
        self.func = func  #传入线程函数逻辑

    def run(self) :
        self.func()

def worker() :
    global SHARE_Q
    while not SHARE_Q.empty():
        top_num = SHARE_Q.get() #获得任务
        douban_url = "http://movie.douban.com/top250?start={page}&filter=&type="
        url = douban_url.format(page = (top_num - 1) * 25)
        my_page = get_page(url)
        find_title(top_num,my_page)  #获得当前页面的电影名
        time.sleep(1)
        SHARE_Q.task_done() # 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号

def get_page(url) :
    """
    根据所给的url爬取网页HTML
    Args: 
        url: 表示当前要爬取页面的url
    Returns:
        返回抓取到整个页面的HTML(unicode编码)
    Raises:
        URLError:url引发的异常
    """
    try :
        my_page = urllib2.urlopen(url).read().decode("utf-8")
    except urllib2.URLError, e :
        if hasattr(e, "code"):
            print "The server couldn't fulfill the request."
            print "Error code: %s" % e.code
        elif hasattr(e, "reason"):
            print "We failed to reach a server. Please check your url and read the Reason"
            print "Reason: %s" % e.reason
    return my_page

def find_title(top_num, my_page) :
    """
    通过返回的整个网页HTML, 正则匹配前100的电影名称
    Args:
        my_page: 传入页面的HTML文本用于正则匹配
    """
    i = top_num * 25 + 1
    temp_data = []
    soup = BeautifulSoup(my_page)
    all_title = soup.find_all('span', class_="title")
    for title in all_title:
        if title.getText().find("/") == -1:
            temp_data.append("Top" + str(i) + " " + title.getText())
            i += 1
    _DATA[top_num] = temp_data


def main() :
    global SHARE_Q
    threads = []
    #向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
    for index in xrange(4) :
        SHARE_Q.put(index)
    for i in xrange(_WORKER_THREAD_NUM) :
        thread = MyThread(worker)
        thread.start()  #线程开始处理任务
        threads.append(thread)
    for thread in threads :
        thread.join()
    SHARE_Q.join() # 意味着等到队列为空，再执行别的操作
    with open("movie.txt", "w+") as my_file :
        for page in _DATA :
            for movie_name in page:
                my_file.write(movie_name + "\n")
    print "Spider Successful!!!"

if __name__ == '__main__':
    main()
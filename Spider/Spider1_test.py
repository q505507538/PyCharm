__author__ = 'Kristine'
# -*- coding:utf-8 -*-
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile(r'<div class="author">\s+<a.*?>\s+<img.*?>\s+(.*?)\s+</a>\s+</div>\s+' +\
                          '<div class="content">\n+(.*?)\n<!--(.*?)-->(.*?)' +\
                          '<div class="stats">\n+<span.*?><i.*?>(.*?)</i>.*?</span>\n+<span.*?>\n+<span.*?>.*?</span>\n+<a.*?>\n+<i.*?>(.*?)</i>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        # print len(item)
        # print item[3]+'\n'
        haveImg = re.search('class="thumb"', item[3])
        if not haveImg:
            print item[0]+'\n', item[1]+'\n', item[2]+'\n', item[4]+'\n', item[5]+'\n'
        else:
            # print item[3]
            p = re.compile(r'<div class="thumb">\n+<a.*?>\n+<img src="(.*?)".*?/>',re.S)
            its = re.findall(p, item[3])
            # print len(its)
            # print its[0]
            print item[0]+'\n', item[1]+'\n', item[2]+'\n', its[0]+'\n', item[4]+'\n', item[5]+'\n'
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

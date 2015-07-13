__author__ = 'Kristine'
# -*- coding:utf-8 -*-
import urllib2
import re

url = 'http://www.8she.com/'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # print content
    pattern = re.compile(r'<header>.*?<i></i></a><h2><a href="(.*?)" title=".*?">(.*?)</a></h2></header>',re.S)
    items = re.findall(pattern, content)
    print len(items)
    for item in items:
        # print len(item)
        print item[0]+'\n', item[1]+'\n'

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

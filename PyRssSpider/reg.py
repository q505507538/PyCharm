# -*- coding: UTF-8 -*-
import re
import PyRssSpider

p = re.compile(r'<h1><a href="(.*?)" data-no-turbolink="true" target="_blank" title="(.*?)">(.*?)</a></h1>')
# print p.split(PyRssSpider.get_html('http://www.91ri.org/', True))

### output ###
# ['one', 'two', 'three', 'four', '']

# print p.findall(PyRssSpider.get_html('http://www.91ri.org/', True))

### output ###
# ['1', '2', '3', '4']

for m in p.finditer(PyRssSpider.get_html('http://www.91ri.org/', True)):
    print m.group()

### output ###
# 1 2 3 4
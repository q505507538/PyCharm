# -*- coding: UTF-8 -*-
import re

str = '<h1><a href="https://www.91ri.org/13377.html" data-no-turbolink="true" target="_blank" title="小技巧：Burp Suite 插件库 BApp Store">小技巧：Burp Suite 插件库 BApp Store</a></h1>sadsadas<h1><a href="https://www.91ri.org/13367.html" data-no-turbolink="true" target="_blank" title="获取运行中的TeamViewer的账号和密码(Test on English GUI)">获取运行中的TeamViewer的账号和密码(Test on English GUI)</a></h1>sdsadsadwqwdzxcz<h1><a href="https://www.91ri.org/13363.html" data-no-turbolink="true" target="_blank" title="php phar LFI">php phar LFI</a></h1>'
p = re.compile(r'<h1><a href="(.*?)" data-no-turbolink="true" target="_blank" title="(.*?)">(.*?)</a></h1>')
# print p.split(str)

### output ###
# ['one', 'two', 'three', 'four', '']

# print p.findall(str)

### output ###
# ['1', '2', '3', '4']

for m in p.finditer(str):
    print m.group()

### output ###
# 1 2 3 4
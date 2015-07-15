# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import re
from PyRssSpider import RssSpider
import datetime

myrss = PyRSS2Gen.RSS2(
    title='elm-world',
    link='http://www.elm-world.com/newpage11.html',
    atom_link='http://117.28.237.21:29956/ording/resource/elm-world.xml',
    description=str(datetime.date.today()),
    lastBuildDate=datetime.datetime.now(),
    language="zh-CN",
    items=[]
)

def main():
    repl1 = {'old': '</a>P<br>', 'new': 'P</a><br>', 'reg': False, 'flags': ''}
    repl2 = {'old': '<BR>\s+</A>', 'new': '</a><br>', 'reg': True, 'flags': re.S|re.I}
    repl3 = {'old': '<A target="_blank" href="extremesex/memder/photo/messi1/index.html"></a><br>', 'new': '', 'reg': False, 'flags': ''}
    replaces = [repl1,repl2,repl3]
    rssSpider = RssSpider(myrss, 'elm-world.xml', charset='CP932')
    items=rssSpider.get_list(r'<a.*?href="(.*?)".*?>(.*?)</a>', remove='<img src="extremesex/memder/ng/logo31.gif" width="47" height="25" border="0" alt="New!">', replaces=replaces, flag=re.S|re.I)
    # print items
    for item in items:
        # print len(item)
        print item[0].decode('CP932')+'\n',item[1].decode('CP932')+'\n'

if __name__ == '__main__':
    main()

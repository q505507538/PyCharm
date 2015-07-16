# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import re
from PyRssSpider import RssSpider
import datetime

myrss = PyRSS2Gen.RSS2(
    title='エルマーWORLD',
    link='http://www.elm-world.com/newpage11.html',
    atom_link='http://117.28.237.21:29956/ording/resource/elm-world.xml',
    description=str(datetime.date.today()),
    lastBuildDate=datetime.datetime.now(),
    language="zh-CN",
    items=[]
)

def main():
    repl0 = {'old': '<img src="extremesex/memder/ng/logo31.gif" width="47" height="25" border="0" alt="New!">', 'new': '', 'reg': False, 'flags': 0}
    repl1 = {'old': '</a>P<br>', 'new': 'P</a><br>', 'reg': False, 'flags': 0}
    repl2 = {'old': '<BR>\s+</A>', 'new': '</a><br>', 'reg': True, 'flags': re.S|re.I}
    repl3 = {'old': '<A target="_blank" href="extremesex/memder/photo/messi1/index.html"></a><br>', 'new': '', 'reg': False, 'flags': 0}
    replaces = [repl0,repl1,repl2,repl3]
    rssSpider = RssSpider(myrss, 'elm-world.xml', charset='CP932')
    rssSpider.get_list(r'<a.*?href="(.*?)".*?>(.*?)</a>', replaces=replaces, flag=re.S|re.I)
    rssSpider.get_content('', '')
    rssSpider.save_rss_file()
    # print items
    # for item in items:
        # print len(item)
        # print item[0]+'\n', item[1].decode('CP932')+'\n'

if __name__ == '__main__':
    main()

# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import PyRssSpider
from PyRssSpider import RssSpider
import datetime

myrss = PyRSS2Gen.RSS2(
    title='91ri',
    link='http://www.91ri.org/',
    atom_link='http://117.28.237.21:29956/ording/resource/91ri.xml',
    description=str(datetime.date.today()),
    lastBuildDate=datetime.datetime.now(),
    language="zh-CN",
    items=[]
)

def main():
    # rssSpider = RssSpider(myrss, '91ri.xml')
    print PyRssSpider.get_html('http://www.91ri.org/', True)


if __name__ == '__main__':
    main()

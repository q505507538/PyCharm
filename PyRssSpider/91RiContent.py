# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import PyRssSpider
from PyRssSpider import RssSpider
import datetime

myrss = PyRSS2Gen.RSS2(
    title='91ri',
    link='https://www.91ri.org/',
    atom_link='http://117.28.237.21:29956/ording/resource/91ri.xml',
    description=str(datetime.date.today()),
    lastBuildDate=datetime.datetime.now(),
    language="zh-CN",
    items=[]
)

def main():
    rssSpider = RssSpider(myrss, '91ri.xml')
    rssSpider.get_list(r'<div class="right-col">\s+<h1><a href="(.*?)" data-no-turbolink="true" target="_blank" title="(.*?)">')
    rssSpider.get_content('<article class="single-post">', '</article>', False)
    rssSpider.SaveRssFile()

if __name__ == '__main__':
    main()

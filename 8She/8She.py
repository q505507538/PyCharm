# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import re, random, datetime
from bs4 import BeautifulSoup

url = "http://www.8she.com/"
host = "www.8she.com"
my_headers = [
    "Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; WOW64; Trident/4.0; SLCC1)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
    "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00",
    "ozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
]


def get_html(url, host, headers):
    random_header = random.choice(headers)
    request = urllib2.Request(url)
    request.add_header("User-Agent", random_header)
    request.add_header("Host", host)
    request.add_header("Referer", "http://baidu.com/")
    request.add_header("GET", url)
    content = urllib2.urlopen(request).read()
    return content


def split(str, beg, end):
    tmp1 = str.split(beg)
    if len(tmp1) == 2:
        tmp2 = tmp1[1].split(end)
        if len(tmp2) == 2:
            return tmp2[0]
    return -1


def split_re(str, beg, end):
    if re.search(beg, str) and re.search(end, str):
        str = re.sub(r'([\s\S]*)' + beg, '', str)
        str = re.sub(end + r'([\s\S]*)', '', str)
        return str
    else:
        return -1;


def get_rss(content):
    myrss = PyRSS2Gen.RSS2(
        title='八社福利站',
        link='http://www.8she.com/',
        atom_link='http://117.28.237.21:29956/ording/resource/8she.xml',
        description='八社福利站',
        lastBuildDate=datetime.datetime.now(),
        language="zh-CN",
        items=[]
    )
    soup = BeautifulSoup(content)
    for x in xrange(1, len(soup.contents)):
        print soup.contents[x].find_all('h2')[0].contents[0].get('href')
        print soup.contents[x].find_all('h2')[0].contents[0].string
        # print soup.contents[x].find_all(class_='note')[0].string
        rss = PyRSS2Gen.RSSItem(
            title=soup.contents[x].find_all('h2')[0].contents[0].string,
            link=soup.contents[x].find_all('h2')[0].contents[0].get('href'),
            comments=soup.contents[x].find_all('h2')[0].contents[0].get('href') + "#comments",
            pubDate=datetime.datetime.now(),
            description=soup.contents[x].find_all(class_='note')[0].string
        )
        myrss.items.append(rss)
    return myrss

def test_rss(content):
    soup = BeautifulSoup(content)
    for x in xrange(1, len(soup.contents)):
      print soup.contents[x].find_all('h2')[0].contents[0].get('href')
      print soup.contents[x].find_all('h2')[0].contents[0].string
      print soup.contents[x].find_all(class_='note')[0].string

def SaveRssFile(myrss, xmlpath):
    finallxml = myrss.to_xml(encoding='utf-8')
    file = open(xmlpath, 'w')
    file.writelines(finallxml)
    file.close()

def main():
    html = get_html(url, host, my_headers).replace('\t', '').replace('\r\n', '').replace('\n', '').replace('\r', '')
    html = re.sub(r'>\s*<', '><', html)
    content = split(html, '<h3> 最新发布</h3>', '<div class="pagination">')
    if content <> -1:
        # test_rss(content)
        SaveRssFile(get_rss(content),"8She.xml")
    else:
        print "获取正文内容失败"

if __name__ == '__main__':
    main()
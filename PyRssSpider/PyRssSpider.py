# -*- coding: UTF-8 -*-
import urllib2
import PyRSS2Gen
import re, random, datetime, sys, os, ssl
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

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

def get_host(url):
    '''
    通过url获取域名
    :param url: 带获取的url地址
    :return:
    '''
    proto, rest = urllib2.splittype(url)
    res, rest = urllib2.splithost(rest)
    if res:
        return res
    else:
        return None

def get_html(url, min):
    '''
    获取网页源代码函数
    :param url: 待获取的url地址
    :param min: 是否精简源代码
    :return:
    '''
    host = get_host(url)
    random_header = random.choice(my_headers)
    request = urllib2.Request(url)
    request.add_header("User-Agent", random_header)
    request.add_header("Host", host)
    request.add_header("Referer", "http://baidu.com/")
    request.add_header("GET", url)
    if url[0:5] == 'https':
        ssl._create_default_https_context = ssl._create_unverified_context
        if get_host(url):
            content = urllib2.urlopen(request).read()
        else:
            print "获取host" + url + "失败"
            return -1
    else:
        if get_host(url):
            content = urllib2.urlopen(request).read()
        else:
            print "获取host" + url + "失败"
            return -1
    if min:
        content = content.replace('\t', '').replace('\r\n', '').replace('\n', '').replace('\r', '')
        content = re.sub(r'>\s*<', '><', content)
        return content
    else:
        return content


def split(str, beg, end):
    tmp1 = str.split(beg)
    # print len(tmp1)
    if len(tmp1) >= 2:
        tmp2 = tmp1[1].split(end)
        # print len(tmp1)
        if len(tmp2) >= 2:
            return tmp2[0]
    return -1


def split_re(str, beg, end):
    if re.search(beg, str) and re.search(end, str):
        str = re.sub(r'([\s\S]*)' + beg, '', str)
        str = re.sub(end + r'([\s\S]*)', '', str)
        return str
    else:
        return -1;

def get_content(self, mode):
    '''
    获取内容
    :return:
    '''
    html = get_html(self.url, True)
    if html <> -1:
        if self.reg:
            content = split_re(html, self.beg, self.end)
        else:
            content = split(html, self.beg, self.end)
        if content <> -1:
            return self.beg + content + self.end
        else:
            print "获取内容失败"
            sys.exit(0)
    else:
        sys.exit(0)

def test_content(self):
    html = get_html(self.url, True)
    if html <> -1:
        if self.reg:
            content = split_re(html, self.beg, self.end)
        else:
            content = split(html, self.beg, self.end)
        if content <> -1:
            return self.beg + content + self.end
        else:
            print "获取正文内容失败"
    else:
        pass

class RssSpider():
    def __init__(self, myrss, xmlpath):
        self.url = myrss.link
        self.myrss = myrss
        self.xmlpath = xmlpath
        if os.path.isfile(self.xmlpath):
            os.remove(self.xmlpath)

    def SaveRssFile(self):
        finallxml = self.myrss.to_xml(encoding='utf-8')
        file = open(self.xmlpath, 'w')
        file.writelines(finallxml)
        file.close()

    def get_content(self, beg, end, reg):
        self.content=[]
        for item in self.list:
            # print len(item)
            print item[0]+'\n', item[1]+'\n'
            html = get_html(item[0], False)
            if html <> -1:
                if reg:
                    content = split_re(html, beg, end)
                else:
                    content = split(html, beg, end)
                if content <> -1:
                    rss = PyRSS2Gen.RSSItem(
                        title='<![CDATA[' + item[1] + ']]>',
                        link=item[0],
                        comments=item[0] + "#comments",
                        pubDate=datetime.datetime.now(),
                        description=beg + content + end
                    )
                    self.myrss.items.append(rss)
                else:
                    print "获取内容失败"
                    sys.exit(0)
            else:
                sys.exit(0)
        for a in self.content:
            print a[0]+'\n', a[1]+'\n', a[2]+'\n',


    def get_list(self, reg):
        pageCode = get_html(self.url, False)
        pattern = re.compile(reg,re.S)
        self.list = re.findall(pattern, pageCode)
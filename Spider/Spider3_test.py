__author__ = 'CQC'
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re

#山东大学绩点运算
class SDU:

    def __init__(self):
        #登录URL
        self.loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
        #本学期成绩URL
        self.gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'stuid':'201200131012',
            'pwd':'xxxxxx'
         })
        #构建opener
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))

    #获取本学期成绩页面
    def getPage(self):
        request  = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        result = self.opener.open(self.gradeUrl)
        #打印登录内容
        print result.read().decode('gbk')


sdu = SDU()
sdu.getPage()
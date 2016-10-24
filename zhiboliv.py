#! /usr/bin/env python
#coding:utf-8
 
import sys
import time
import re
import urllib2
import urllib
import requests
import cookielib
from bs4 import BeautifulSoup
import logingjj
 
## 这段代码是用于解决中文报错的问题  

reqURL = 'http://www.zhibo8.cc/'

class GetInfo(object):
     
    def __init__(self):
        self.opener = urllib2.build_opener() 
        urllib2.install_opener(self.opener)    
     
    def getInfo(self):
	'''请求内容'''
      
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'}
      
	response = urllib2.urlopen(reqURL)
	#html.decode(网页编码).encode(系统编码) 
        thePage = response.read().decode('utf-8').encode(sys.getfilesystemencoding())   

	thisPageSoup = BeautifulSoup(thePage)
	
	for thisOneNameContent in thisPageSoup.find_all("li", attrs={"label":re.compile(ur".*"+keyWord+".*")}) :
		print thisOneNameContent["data-time"]+"  "+thisOneNameContent.b.get_text()

		print '#########################################################'+'\n'
		
		
         
if __name__ == '__main__': 

	reload(sys) 
	sys.setdefaultencoding("utf-8")

	keyWord= '利物浦'

	if   (len(sys.argv)==2) :
		keyWord= sys.argv[1]
	
	print '以下是'+keyWord+'近期的赛事'

	getInfo = GetInfo()
	getInfo.getInfo()

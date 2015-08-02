# coding=utf-8
import urllib2
import urllib
from lxml import etree
from urllib2 import URLError
import lxml.html
import xlwt
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getUrlContent(url):
  try:
    myhtml = urllib2.urlopen(url).read()
    page = lxml.html.fromstring(myhtml)
    if len(page.xpath(u'//div[@id="contentArea"]')) == 0:
        return ""
    node = page.xpath(u'//div[@id="contentArea"]')[0]

    text = ""
    
    for mynode in node.iter():
        if mynode.text == None:
            continue
        
            text = text + str(child.text)
        text = text + str(mynode.text) + "\n"
  except Exception, e:
	  return ""
  return text

url = "http://www.ajxxgk.jcy.gov.cn/html/20150710/2/802751.html"
# print getUrlContent(url)

from pyquery import PyQuery as pq
doc=pq(url)
data=doc('.MsoNormal')
lineno = 0
text = ""
for i in data:
    lineno += 1
    text += pq(i).text() + "\n"
print text


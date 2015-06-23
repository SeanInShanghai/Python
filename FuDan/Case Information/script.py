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


query_entries = ['贪污', '行贿', '受贿', '挪用公款', '巨额财产来源不明', '职务侵占']
page_number = 0
execel_file = xlwt.Workbook()
current_sheet = None
execlLineNo = 0
curDir = None

tmplateUrl = "http://www.ajxxgk.jcy.gov.cn/index.php?m=search&c=index&a=init&typeid=&q=%s&siteid=1&newstypeid=54&time=all&page=%d"
# tmplateUrl = tmplateUrl %('受贿', 2)
base_url = "http://www.ajxxgk.jcy.gov.cn"

myhtml = urllib2.urlopen(tmplateUrl).read()
page = lxml.html.fromstring(myhtml)
node = page.xpath(u'//ul[@class="wrap"]')[0]
pageValid = True
lineno = 0

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
        text = text + str(mynode.text) + "\n"
  except Exception, e:
	  return ""
  return text
    
def getPageInfo(tmplateUrl):
    global curDir
    myhtml = urllib2.urlopen(tmplateUrl).read()
    page = lxml.html.fromstring(myhtml)
    node = page.xpath(u'//ul[@class="wrap"]')[0]
    result = []
    lineno = 0
    item = []
    for mynode in node.iter():
        # print mynode.text, lineno
        
        if lineno == 0:
            lineno += 1
            continue
        if 5 == (lineno % 8):
            title = str(mynode.text) + curDir + "案"
            if '（' in title:
                title = title + "）"
            item.append(title)
            if 'href' not in mynode.attrib.keys():
                item.append("")
                item.append("no url")
                lineno += 1
                continue
             
            haltUrl = mynode.attrib['href']
            url = base_url+haltUrl
            content = getUrlContent(url)
            item.append(content)
            item.append(url)
        elif 6 == (lineno % 8):
            item.append(mynode.text)
            # print mynode.text, lineno
        elif lineno % 8 == 0:
	        item.append(mynode.text)
	        result.append(item)
	        item = []
	        # print mynode.text, lineno, "end \n"
        
        lineno += 1
        # print mynode.text, lineno
    
    
    return result

def writeToExecel(result):
    global current_sheet
    global execlLineNo
    global curDir
    
    for item in result:
        itemLen = len(item)
        execlLineNo += 1
        for i in range(itemLen):
            # print execlLineNo,i
            text = item[i]
            if 1 == i:
                os.chdir(curDir)
                newfile = open(str(execlLineNo)+".txt", 'w')
                if None == item[i]:
                    item[i] = "null"
                content = item[i].decode('utf-8')
                newfile.write(content)
                newfile.close()
                os.chdir('..')
                text = str(execlLineNo)+".txt"
            current_sheet.write(execlLineNo, i, text.decode('utf-8'))
            
    
for query_entry in query_entries:
	
    current_sheet = execel_file.add_sheet(query_entry.decode('utf-8'), cell_overwrite_ok = True)
    current_sheet.write(0, 0, 'title')
    current_sheet.write(0, 1, 'content_file')
    current_sheet.write(0, 2, 'url')
    current_sheet.write(0, 3, 'type')
    current_sheet.write(0, 4, 'time')
    
    page_number = 0
    execlLineNo = 0
    curDir = query_entry
    if not os.path.isdir(curDir):
        os.mkdir(curDir)
    
    while True:
        page_number += 1
        # print tmplateUrl
        # print "hhh"
        curUrl = tmplateUrl % (str(query_entry), page_number)
        try:
            exce_test = urllib2.urlopen(curUrl)
            
            result = getPageInfo(curUrl)
            writeToExecel(result)
        except URLError, e:
            print tmplateUrl
            print e
            pageValid = False
        # if 1 == page_number:
		# 	pageValid = False
		# 	break
        
        if not pageValid:
            break
    
    # if not pageValid:
	# 	break
    
execel_file.save('test.xls')		

#coding=utf-8
import urllib2
import urllib
from lxml import etree
import lxml.html
from urllib2 import URLError
import xlwt
import os
from docx import Document
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
output = open('data.txt', 'w')
execlOutput = xlwt.Workbook()
sheetList = ['行贿', '受贿', '贪污', '挪用', '滥用职权', '职务侵占']

def getUrlContent(url):
	myhtml = urllib2.urlopen(url).read()
	page = lxml.html.fromstring(myhtml)
	node = page.xpath(u'//div[@id="PrintArea"]')[0]
	lineno = 0
	text = ''
	courtName = ''
	for mynode in node.iter():
		if lineno < 3:
			lineno += 1 
			continue
		if 3 == lineno:
			courtName = mynode.text
		lineno += 1
		text = text + str(mynode.text) + '\n'
	return text, courtName

def getResult(node):
	result = []
	lineno = 0
	item = []
	for mynode in node.iter():
		#print mynode.text, i
		
		if lineno < 12:
			lineno += 1
			continue
		else:
			text = str(mynode.text)
			text = "".join(text.split())
			tmpLineNo = lineno - 12
			tmp = tmpLineNo % 7
			
			if 1 == tmp:
				item.append(text)
			elif 2 == tmp:
				item.append(text)
			elif 4 == tmp:
				item.append(text)
				
				curUrl = mynode.attrib['href']
				item.append(curUrl)
				urlContent, courtName = getUrlContent(curUrl)
				item.append(urlContent)
				item.append(courtName)
			elif 5 == tmp:
				item.append(text)
			elif 6 == tmp:
				item.append(text)
				result.append(item)
				item = []
		  
		# print 'myline: ', lineno
		lineno += 1
	return result


def writeResultToSheet(result, sheet):
    global execlLineNo
    global curDir
    for item in result:
        execlLineNo += 1
        itemLen = len(item)
        for i in range(itemLen):
	
            text = item[i]
            if i == 4:
				
                #doc = Document()
                #doc.add_paragraph(text.decode('utf-8'))
                #os.chdir(curDir)
                #doc.save(str(execlLineNo)+".docx")
                #os.chdir('..')
                #text = str(execlLineNo)+".docx"
                
                os.chdir(curDir)
                newfile = open(str(execlLineNo)+".txt", 'w')
                if None == text:
					text = "Null"
                text = text.decode('utf-8')
                newfile.write(text)
                newfile.close()
                os.chdir('..')
                text = str(execlLineNo)+".txt"
                
            # print execlLineNo, i
            sheet.write(execlLineNo, i, text.decode('utf-8'))



baseUrl = 'http://www.court.gov.cn/extension/simpleSearch.htm'
execlLineNo = 0
curDir = ""
#headers = {  
#    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
#} 
for sheetName in sheetList:
    curSheet = execlOutput.add_sheet(sheetName.decode('utf-8'), cell_overwrite_ok = True)
    curSheet.write(0, 0, 'no')
    curSheet.write(0, 1, 'court')
    curSheet.write(0, 2, 'title')
    curSheet.write(0, 3, 'url')
    curSheet.write(0, 4, 'content')
    curSheet.write(0, 5, 'court name')
    curSheet.write(0, 6, 'case number')
    curSheet.write(0, 7, 'date')
    
    execlLineNo = 0
    
    keyword = sheetName
    pageNo = 1
    pageValid = True
    
    curDir = sheetName
    if not os.path.isdir(curDir):
        os.mkdir(curDir)
    
    while True:
        try:
            values = {'keyword':keyword, 
                      'page':pageNo}
      
            data = urllib.urlencode(values)
            req = urllib2.Request(baseUrl+'?'+data)
            response = urllib2.urlopen(req)
            
            myhtml = response.read()
            page = etree.HTML(myhtml.lower().decode('utf-8'))
            node = page.xpath(u"//table[@class='tablestyle']")[0]
            result = getResult(node)
            writeResultToSheet(result, curSheet)
        except URLError, e:
            print e
            pageValid = False

        #if pageNo == 2:
		#	pageValid = False

        if not pageValid:
            break
            
        pageNo += 1

    print sheetName
    #if sheetName == '受贿':
	#	break
    if not pageValid:
		continue
execlOutput.save('second.xls')
# print myhtml
